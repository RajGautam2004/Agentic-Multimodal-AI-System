"""
FastAPI Backend for Multimodal RAG System with Llama-3.2

This module provides REST API endpoints for the RAG (Retrieval-Augmented Generation)
pipeline with multimodal document support.
"""

import os
from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# LlamaIndex imports
from llama_index.core import VectorStoreIndex, StorageContext, Settings
from llama_index.core.node_parser import SentenceSplitter
from llama_index.vector_stores.milvus import MilvusVectorStore
from llama_index.embeddings.nvidia import NVIDIAEmbedding
from llama_index.llms.huggingface import HuggingFaceLLM

# RAG pipeline imports
from rag.enhanced_pipeline import enhanced_rag


# ===================== FastAPI Setup =====================
app = FastAPI(
    title="Multimodal RAG API",
    description="Agentic Multimodal RAG System with Llama-3.2",
    version="1.0.0"
)


# ===================== Pydantic Models =====================
class QueryRequest(BaseModel):
    """Request model for RAG queries."""
    query: str = Field(..., description="The query to process", min_length=1)
    top_k: Optional[int] = Field(default=3, description="Number of top results to retrieve")


class QueryResponse(BaseModel):
    """Response model for RAG queries."""
    query: str
    response: str
    source_count: int = 0


# ===================== Global Variables =====================
# These will be initialized when the app starts
retriever = None
llm = None
index = None


# ===================== Initialization Functions =====================
def initialize_embeddings():
    """Initialize NVIDIA embeddings for vector search."""
    try:
        embeddings = NVIDIAEmbedding(
            model_name="nvidia/NV-Embed-v2",
            api_key=os.getenv("NVIDIA_API_KEY"),
        )
        return embeddings
    except Exception as e:
        print(f"Warning: Could not initialize NVIDIA embeddings: {e}")
        print("Falling back to default embeddings...")
        return None


def initialize_vector_store():
    """Initialize Milvus vector store for document storage."""
    try:
        # Configure Milvus connection
        vector_store = MilvusVectorStore(
            uri="http://localhost:19530",  # Default Milvus URI
            collection_name="documents",
            chunk_size=1024,
            overwrite=False,
        )
        return vector_store
    except Exception as e:
        print(f"Warning: Could not initialize Milvus vector store: {e}")
        print("Consider starting Milvus or configuring the correct URI...")
        return None


def initialize_llm():
    """Initialize HuggingFace LLM (Llama-3.2-3B-Instruct)."""
    try:
        model_id = "meta-llama/Llama-3.2-3B-Instruct"
        llm = HuggingFaceLLM(
            model_name=model_id,
            tokenizer_name=model_id,
            context_window=8192,
            model_kwargs={
                "torch_dtype": "auto",
                "load_in_8bit": True,  # Enable quantization to save memory
            },
            generate_kwargs={
                "temperature": 0.7,
                "top_p": 0.95,
                "max_new_tokens": 512,
            },
        )
        return llm
    except Exception as e:
        print(f"Error initializing LLM: {e}")
        raise RuntimeError(f"Could not initialize LLM: {e}")


def initialize_retriever(vector_store=None):
    """Initialize retriever from vector store or memory."""
    try:
        if vector_store:
            # Use Milvus-backed retriever
            storage_context = StorageContext.from_defaults(vector_store=vector_store)
            index = VectorStoreIndex.from_documents(
                [],  # Start with empty index, populate with documents later
                storage_context=storage_context,
                show_progress=True,
            )
        else:
            # Use in-memory index (for testing)
            index = VectorStoreIndex([])
        
        retriever = index.as_retriever(similarity_top_k=3)
        return retriever, index
    except Exception as e:
        print(f"Error initializing retriever: {e}")
        raise RuntimeError(f"Could not initialize retriever: {e}")


# ===================== Startup Event =====================
@app.on_event("startup")
async def startup_event():
    """Initialize RAG pipeline on app startup."""
    global retriever, llm, index
    
    print("Initializing RAG Pipeline...")
    
    try:
        # Initialize embeddings
        embeddings = initialize_embeddings()
        if embeddings:
            Settings.embed_model = embeddings
        
        # Initialize vector store (optional - will fall back to in-memory)
        vector_store = initialize_vector_store()
        
        # Initialize LLM
        llm = initialize_llm()
        Settings.llm = llm
        print("✓ LLM initialized")
        
        # Initialize retriever and index
        retriever, index = initialize_retriever(vector_store)
        print("✓ Retriever initialized")
        
        print("✓ RAG Pipeline ready!")
        
    except Exception as e:
        print(f"✗ Startup Error: {e}")
        raise RuntimeError(f"Failed to initialize RAG pipeline: {e}")


# ===================== Health Check Endpoint =====================
@app.get("/health")
async def health_check():
    """Check if the API is running and initialized."""
    is_ready = retriever is not None and llm is not None
    return {
        "status": "healthy" if is_ready else "initializing",
        "retriever_ready": retriever is not None,
        "llm_ready": llm is not None,
    }


# ===================== RAG Query Endpoint =====================
@app.post("/ask", response_model=QueryResponse)
async def ask_question(req: QueryRequest):
    """
    Process a query using the RAG pipeline.
    
    The pipeline:
    1. Decomposes complex queries into sub-queries
    2. Retrieves relevant documents for each sub-query
    3. Combines context and generates a response using the LLM
    
    Args:
        req: QueryRequest containing the user query
        
    Returns:
        QueryResponse with the generated response
        
    Raises:
        HTTPException: If RAG pipeline is not initialized or processing fails
    """
    if retriever is None or llm is None:
        raise HTTPException(
            status_code=503,
            detail="RAG pipeline not initialized. Please try again later."
        )
    
    try:
        # Process query through RAG pipeline
        response = enhanced_rag(req.query, retriever, llm)
        
        # Convert response to string if needed
        response_text = str(response) if response else "No response generated"
        
        return QueryResponse(
            query=req.query,
            response=response_text,
            source_count=0,  # This can be enhanced to track actual sources
        )
        
    except Exception as e:
        print(f"Error processing query: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Error processing query: {str(e)}"
        )


# ===================== Document Management Endpoint =====================
@app.post("/documents/add")
async def add_documents(documents: list):
    """
    Add documents to the RAG index.
    
    Args:
        documents: List of document objects with 'text' and optional 'metadata'
        
    Returns:
        Confirmation of documents added
    """
    if index is None:
        raise HTTPException(
            status_code=503,
            detail="Index not initialized"
        )
    
    try:
        from llama_index.core import Document
        
        doc_objects = [
            Document(text=doc.get("text", ""), metadata=doc.get("metadata", {}))
            for doc in documents
        ]
        
        index.insert_nodes(doc_objects)
        
        return {
            "status": "success",
            "documents_added": len(documents)
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error adding documents: {str(e)}"
        )


# ===================== Root Endpoint =====================
@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "name": "Multimodal RAG API",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "ask": "/ask (POST)",
            "add_documents": "/documents/add (POST)",
            "docs": "/docs (Swagger UI)",
        }
    }


# ===================== Run Instructions =====================
if __name__ == "__main__":
    import uvicorn
    
    # Run: uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
    uvicorn.run(
        "backend.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
