# QUICK_START.md

# Quick Start - Multimodal RAG API

## 1. Install & Setup (One-time)
```bash
# Install dependencies
pip install -r requirements.txt

# Setup environment file
copy .env.example .env
# Edit .env with your API keys
```

## 2. Run the API
```bash
# From project root directory
python -m uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

## 3. Test the API

**Health check:**
```bash
curl http://localhost:8000/health
```

**Ask a question:**
```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"query": "What is artificial intelligence?"}'
```

**Interactive testing:**
Open browser: http://localhost:8000/docs

## Project Structure (Fixed)

```
backend/
  ├── main.py              # ✓ Fixed - Proper initialization
  └── config.py            # Configuration settings

rag/
  ├── enhanced_pipeline.py # ✓ Fixed - Correct imports

agents/
  ├── planner.py           # ✓ Fixed - Correct imports
  └── reasoning_agent.py   # ✓ Fixed - No undefined variables

app.py                     # Streamlit UI (at root)

requirements.txt           # ✓ Updated with FastAPI & Uvicorn
```

## All Errors Fixed ✓

| Error | Fix |
|-------|-----|
| Import fastapi could not be resolved | ✓ Added to requirements.txt |
| Import rag.enhanced_pipeline failed | ✓ Moved file & fixed imports |
| retriever is not defined | ✓ Initialized in startup event |
| llm is not defined | ✓ Initialized with HuggingFaceLLM |
| Package structure issues | ✓ Created with __init__.py files |

## What Each File Does

**backend/main.py** - FastAPI app with:
- Proper LLM initialization (Llama-3.2-3B)
- Retriever setup (in-memory or Milvus)
- RAG query endpoint
- Health checks
- Error handling

**rag/enhanced_pipeline.py** - RAG orchestration that:
- Receives queries
- Calls agents for decomposition
- Returns llm responses

**agents/planner.py** - Orchestrates:
- Query decomposition
- Document retrieval
- Context combination

**agents/reasoning_agent.py** - Decomposes:
- Complex queries into sub-queries
- Ready for OpenAI integration

## Environment Variables (.env)

```
NVIDIA_API_KEY=your_key_here
HF_TOKEN=your_hf_token
API_PORT=8000
```

See `.env.example` for all available options.

## Common Issues & Fixes

**"ModuleNotFoundError: No module named 'backend'"**
- Make sure running from project root
- Use: `python -m uvicorn backend.main:app --reload`

**"retriever/llm not initialized"**
- Check startup logs for errors
- Call `/health` endpoint to verify initialization

**Memory issues with Llama model**
- Already configured with 8-bit quantization
- Requires ~6-8GB VRAM

**Milvus connection fails**
- Optional - system falls back to in-memory index
- Start Milvus: `docker run -d -p 19530:19530 milvusdb/milvus:latest`

---

**Ready to go!** Start the server and visit http://localhost:8000/docs
