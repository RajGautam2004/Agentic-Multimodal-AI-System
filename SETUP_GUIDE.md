# SETUP_GUIDE.md

# Multimodal RAG System - Setup Guide

## Project Structure

After the fix, your project structure should be:

```
Multimodal-RAG-with-Llama-3.2-main/
├── backend/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application (MOVED from root)
│   └── config.py               # Configuration settings
├── rag/
│   ├── __init__.py
│   ├── enhanced_pipeline.py    # RAG pipeline (MOVED from root)
├── agents/
│   ├── __init__.py
│   ├── planner.py              # Query planner (MOVED from root)
│   └── reasoning_agent.py       # Query decomposer (MOVED from root)
├── app.py                        # Streamlit app (at root)
├── document_processors.py        # Document processing (at root)
├── utils.py                      # Utilities (at root)
├── requirements.txt              # Fixed with FastAPI & Uvicorn
├── .env.example                  # Environment configuration template
└── README.md
```

## Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Key packages added:
- **fastapi==0.109.0** - REST API framework
- **uvicorn==0.27.0** - ASGI server
- **pydantic==2.5.3** - Data validation

## Step 2: Setup Environment Variables

```bash
# Copy the template
copy .env.example .env

# Edit .env and add your API keys:
# - NVIDIA_API_KEY (for embeddings)
# - HF_TOKEN (for HuggingFace models)
# - OPENAI_API_KEY (optional, for advanced query decomposition)
```

## Step 3: (Optional) Start Milvus Vector Database

If you want to use persistent vector storage with Milvus:

### Option A: Docker (Recommended)
```bash
docker run -d \
  --name milvus \
  -p 19530:19530 \
  -p 9091:9091 \
  milvusdb/milvus:latest
```

### Option B: Local Installation
Follow: https://milvus.io/docs/install_standalone.md

## Step 4: Run the FastAPI Backend

### Development mode (with auto-reload):
```bash
cd Multimodal-RAG-with-Llama-3.2-main
python -m uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

### Production mode:
```bash
python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000 --workers 4
```

The API will be available at: **http://localhost:8000**

## Step 5: Test the API

### Health Check:
```bash
curl http://localhost:8000/health
```

### Ask a Question:
```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"query": "What is machine learning?"}'
```

### Interactive API Docs:
Open your browser and go to: **http://localhost:8000/docs**

This opens Swagger UI where you can test all endpoints interactively.

## Step 6: (Optional) Run Streamlit App

In a separate terminal:
```bash
streamlit run app.py
```

## Fixed Issues

### ✅ Import Errors Fixed:
- ✓ `fastapi` now in requirements.txt
- ✓ `uvicorn` now in requirements.txt  
- ✓ `rag.enhanced_pipeline` import paths fixed
- ✓ `agents.planner` import paths fixed
- ✓ Package structure created with `__init__.py` files

### ✅ Undefined Variables Fixed:
- ✓ `retriever` - Now initialized in startup event
- ✓ `llm` - Now initialized with HuggingFaceLLM
- ✓ Both are properly loaded before handling requests

### ✅ File Organization:
- ✓ `main.py` moved to `backend/` folder
- ✓ `enhanced_pipeline.py` moved to `rag/` folder
- ✓ `planner.py` and `reasoning_agent.py` moved to `agents/` folder
- ✓ Proper Python package structure established

## Troubleshooting

### Issue: "module not found" errors
**Solution:** Make sure you're running from the project root directory and have run `pip install -r requirements.txt`

### Issue: NVIDIA embeddings not initializing
**Solution:** Set `NVIDIA_API_KEY` in .env or the fallback will use default embeddings

### Issue: Milvus connection failed
**Solution:** Either start Milvus with Docker or comment out Milvus initialization. The system will fall back to in-memory index.

### Issue: Out of memory loading Llama model
**Solution:** The config.py has `load_in_8bit: True` for quantization. Make sure you have at least 8GB VRAM or increase system RAM.

### Issue: HuggingFace model download fails
**Solution:** 
```bash
huggingface-cli download meta-llama/Llama-3.2-3B-Instruct
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API information |
| GET | `/health` | Health check |
| POST | `/ask` | Ask a question using RAG |
| POST | `/documents/add` | Add documents to index |
| GET | `/docs` | Swagger UI documentation |

## Development Tips

1. **Auto-reload enabled** in development mode - changes to Python files will auto-restart the server
2. **Swagger UI** available at `/docs` for interactive testing
3. **Detailed logs** - Check console output for initialization and processing steps
4. **Query decomposition** - Can be enabled by setting OpenAI API key for advanced multi-step queries

## Next Steps

1. Add your documents to the vector store
2. Customize the LLM parameters in `backend/config.py`
3. Extend query decomposition with OpenAI (set `OPENAI_API_KEY`)
4. Deploy to production with proper error handling and monitoring
