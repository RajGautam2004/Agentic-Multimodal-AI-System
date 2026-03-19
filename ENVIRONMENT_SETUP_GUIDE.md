# ENVIRONMENT_SETUP_GUIDE.md

# Complete Environment & Dependency Setup Guide

## Current System Info
- **Python Version:** 3.12.1
- **OS:** Windows (your system)
- **Project:** Multimodal Agentic RAG System with Llama-3.2

---

## Problems Found & Solutions

### Problem 1: Python 3.12 Compatibility
**Issue:** Many packages don't officially support Python 3.12 yet
- ❌ `pymilvus` - Requires Python <3.12
- ❌ `llama-index-embeddings-nvidia` - Old versions incompatible
- ❌ Exact version pinning causes conflicts

**Solution:** Use flexible version constraints (allows pip to resolve compatible versions)

---

## Installation Options

### OPTION 1: Quick Install (Recommended for Python 3.12)

```bash
# Use the simplified requirements file with flexible versions
cd "c:\Users\rajga\OneDrive\var\Multimodal-RAG-with-Llama-3.2-main"

pip install -r requirements-simple.txt
```

**This file uses flexible versions** that pip can automatically resolve for Python 3.12.

---

### OPTION 2: Virtual Environment (Best Practice)

If you want a fresh, isolated environment:

```bash
# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate

# Install dependencies
pip install -r requirements-simple.txt
```

**Advantages:**
- ✓ Clean, isolated environment
- ✓ No conflicts with system packages
- ✓ Easy to reset if issues occur

---

### OPTION 3: Conda Environment (For Complex Dependencies)

If you have Anaconda/Miniconda installed:

```bash
# Create environment
conda create -n multimodal python=3.10

# Activate
conda activate multimodal

# Install from pip
pip install -r requirements-simple.txt
```

**Why Python 3.10?** Better compatibility with ML packages like PyTorch and LlamaIndex

---

## File Structure After Setup

```
Multimodal-RAG-with-Llama-3.2-main/
│
├── backend/
│   ├── __init__.py           ✓ Fixed
│   ├── main.py               ✓ Fixed (FastAPI app)
│   └── config.py             ✓ New config file
│
├── rag/
│   ├── __init__.py           ✓ Fixed
│   └── enhanced_pipeline.py  ✓ Fixed
│
├── agents/
│   ├── __init__.py           ✓ Fixed
│   ├── planner.py            ✓ Fixed
│   └── reasoning_agent.py    ✓ Fixed
│
├── .env.example              ✓ New template
├── requirements.txt          ✓ Updated (strict versions)
├── requirements-simple.txt   ✓ New (flexible versions - USE THIS)
├── SETUP_GUIDE.md            ✓ Detailed setup
├── QUICK_START.md            ✓ Quick reference
├── ENVIRONMENT_SETUP_GUIDE.md ✓ This file
│
├── app.py                    Original Streamlit app
├── document_processors.py    Original utilities
├── utils.py                  Original utilities
└── README.md
```

---

## Dependency Explanations

### Core Web Framework
| Package | Purpose | Min Version |
|---------|---------|------------|
| `fastapi` | REST API framework | 0.100+ |
| `uvicorn` | ASGI server | 0.20+ |
| `pydantic` | Data validation | 2.0+ |

### Document Processing
| Package | Purpose | Min Version |
|---------|---------|------------|
| `pymupdf` | PDF extraction | 1.23+ |
| `python-pptx` | PowerPoint processing | 0.6+ |
| `Pillow` | Image processing | 10.0+ |

### RAG & LLM
| Package | Purpose | Min Version |
|---------|---------|------------|
| `llama-index-core` | RAG orchestration | 0.9+ |
| `llama-index-readers-file` | File readers | 0.1+ |
| `llama-index-llms-huggingface` | HF LLM integration | 0.1+ |

### Deep Learning
| Package | Purpose | Min Version |
|---------|---------|------------|
| `torch` | PyTorch ML framework | 2.0+ |
| `transformers` | HuggingFace models | 4.30+ |
| `numpy` | Numerical computing | Must be <2.0 for compatibility |

---

## Step-by-Step Installation

### Step 1: Verify Python Version
```bash
python --version
# Should show: Python 3.12.1 or similar
```

### Step 2: Upgrade pip, setuptools, wheel
```bash
python -m pip install --upgrade pip setuptools wheel
```

### Step 3: Create Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 4: Install Dependencies
```bash
# Navigate to project directory
cd "c:\Users\rajga\OneDrive\var\Multimodal-RAG-with-Llama-3.2-main"

# Install using flexible version file
pip install -r requirements-simple.txt

# If that fails, install core packages one by one:
pip install fastapi uvicorn pydantic
pip install pymupdf python-pptx Pillow requests streamlit
pip install llama-index-core llama-index-readers-file
pip install llama-index-llms-huggingface
pip install torch transformers numpy scikit-learn
pip install python-dotenv
```

### Step 5: Verify Installation
```bash
# Check key packages
pip list | findstr fastapi
pip list | findstr torch
pip list | findstr llama

# Or test imports
python -c "import fastapi; import torch; print('✓ Installation successful')"
```

---

## Common Issues & Fixes

### Issue 1: "File is being used by another process"
**Cause:** Another Python process is holding file locks
**Fix:**
```bash
# Kill all Python processes
taskkill /F /IM python.exe

# Wait a moment, then try install again
pip install -r requirements-simple.txt
```

### Issue 2: "No matching distribution found"
**Cause:** Strict version constraints that don't exist
**Fix:**
```bash
# Use flexible version file instead
pip install -r requirements-simple.txt

# NOT the strict one:
# pip install -r requirements.txt  # ❌ Don't use this
```

### Issue 3: "Requires-Python <3.12" Error
**Cause:** Package doesn't support Python 3.12
**Fix:**
- ✓ Use `requirements-simple.txt` (flexible versions)
- ✓ Downgrade Python to 3.10 or 3.11
- ✓ Skip that specific package if optional

### Issue 4: "numpy <2.0" Conflict
**Cause:** NumPy 2.0 breaks many older packages
**Fix:**
```bash
pip install "numpy<2.0"
```

### Issue 5: Module Import Errors After Install
**Cause:** Virtual environment not activated
**Fix:**
```bash
# Activate virtual environment
venv\Scripts\activate

# Or use system Python if no venv
python -m pip --version
```

---

## Environment Variables (.env)

Create `.env` file from template:
```bash
copy .env.example .env
```

Edit `.env` with your values:
```
NVIDIA_API_KEY=your_nvidia_key_here
HF_TOKEN=your_huggingface_token
API_HOST=0.0.0.0
API_PORT=8000
```

---

## Testing the Installation

### 1. Test FastAPI Backend
```bash
cd "c:\Users\rajga\OneDrive\var\Multimodal-RAG-with-Llama-3.2-main"

# Start the server
python -m uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

Visit: http://localhost:8000/docs

### 2. Test Streamlit Frontend
```bash
# In a new terminal
streamlit run app.py
```

### 3. Test Imports
```bash
python -c "
from backend.main import app
from rag.enhanced_pipeline import enhanced_rag
from agents.planner import plan_and_execute
print('✓ All imports working!')
"
```

---

## Troubleshooting Checklist

- [ ] Python version is 3.12.1 or compatible
- [ ] Using `requirements-simple.txt` (not `requirements.txt`)
- [ ] Pip is upgraded: `pip --version` shows 26+ or latest
- [ ] No Python processes are running before install
- [ ] Virtual environment is activated (if using one)
- [ ] All files created in correct folders (backend/, rag/, agents/)
- [ ] `.env.example` copied to `.env`
- [ ] Can import packages: `python -c "import fastapi; import torch"`

---

## Next Steps

1. **Install dependencies:** `pip install -r requirements-simple.txt`
2. **Setup environment:** `copy .env.example .env` then edit
3. **Start FastAPI:** `python -m uvicorn backend.main:app --reload`
4. **Test API:** Visit http://localhost:8000/docs
5. **Push to Git:** 
   ```bash
   git add .
   git commit -m "Fix: Complete environment setup with corrected dependencies"
   git push origin main
   ```

---

## Summary of Fixes Applied

✅ **Folder Structure:** Created proper package directories (backend/, rag/, agents/)
✅ **Import Paths:** Fixed all relative imports to match new structure  
✅ **Undefined Variables:** Initialized `retriever` and `llm` in startup
✅ **Requirements:** Updated with FastAPI, Uvicorn, Pydantic
✅ **Python 3.12:** Created flexible requirements file for compatibility
✅ **Virtual Environment:** Instructions for isolated setups
✅ **Configuration:** Added `.env` template and config.py
✅ **Documentation:** Created comprehensive setup guides

---

**You're ready to go!** Use `requirements-simple.txt` for installation on Python 3.12.
