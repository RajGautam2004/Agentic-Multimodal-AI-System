# rag/enhanced_pipeline.py
"""Enhanced RAG pipeline using agent-based decomposition and retrieval."""

from agents.planner import plan_and_execute


def enhanced_rag(query, retriever, llm):
    """
    Enhanced RAG function that decomposes queries and retrieves context.
    
    Args:
        query: User query string
        retriever: LlamaIndex retriever instance
        llm: LlamaIndex LLM instance
        
    Returns:
        Response from LLM based on retrieved context
    """
    return plan_and_execute(query, retriever, llm)
