<<<<<<< HEAD
# Agentic-Multimodal-AI-System
A next-gen multimodal AI system that understands text, images, and context using agentic reasoning and advanced RAG pipelines.
=======
# 🚀 Multimodal Agentic RAG System with Llama 3.2

## 🧠 Overview

This project extends a Multimodal RAG system into a **research-level AI system** by integrating:

* 🔍 Retrieval-Augmented Generation (RAG)
* 🧠 Reasoning (Query Decomposition)
* 🤖 Agent-based pipeline
* 🖼️ Multimodal understanding (text + images)

The system leverages **Llama 3.2 (LLM + Vision)** to process and understand:

* PDFs
* PowerPoint files
* Images
* Text documents

It enables users to query complex multimodal data with **reasoning-enhanced responses**.

---

## 🔥 Key Upgrades (What Makes This Unique)

Unlike basic RAG systems, this project introduces:

### 🧠 Reasoning-First Retrieval

* Breaks user queries into sub-questions
* Performs multi-step retrieval

### 🤖 Agent-Based Pipeline

* Planner + Retriever + Generator workflow
* Improves answer quality

### 🔁 Multi-Step RAG

* Retrieve → refine → generate
* Better context understanding

---

## 🏗️ System Architecture

```text
User Query
   ↓
Reasoning Agent (Query Decomposition)
   ↓
Retriever (Vector DB - Milvus)
   ↓
Context Aggregation
   ↓
LLM (Llama 3.2)
   ↓
Final Answer
```

---

## ⚙️ Tech Stack

* **LLM**: Llama 3.2 (HuggingFace)
* **Vision Model**: Llama 3.2 Vision
* **Framework**: LlamaIndex
* **Vector DB**: Milvus
* **Embeddings**: NVIDIA Embeddings
* **Frontend**: Streamlit
* **Reasoning Layer**: Custom Agent Pipeline

---

## 🚀 Features

* 📄 Multi-format document ingestion (PDF, PPT, images)
* 🖼️ Image + chart understanding (DePlot + VLM)
* 🔍 Vector-based semantic search
* 💬 Chat interface
* 🧠 Query decomposition (reasoning)
* 🤖 Agent-driven RAG pipeline

---

## 📁 Project Structure

```
.
├── app.py
├── document_processors.py
├── utils.py
├── rag/
│   └── enhanced_pipeline.py
├── agents/
│   ├── reasoning_agent.py
│   └── planner.py
├── requirements.txt
```

---

## 🛠️ Setup

### 1. Clone the repo

```
git clone <your-repo-url>
cd <repo-folder>
```

---

### 2. Create environment

#### Conda:

```
conda create --name multimodal-agent python=3.10
conda activate multimodal-agent
```

#### OR venv:

```
python -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Set NVIDIA API Key

```
export NVIDIA_API_KEY="your-api-key"
```

---

### 5. Start Milvus (Docker)

```
docker compose up -d
```

---

## ▶️ Run Application

```
streamlit run app.py
```

---

## 🧪 Usage

1. Upload files or provide directory
2. Process documents
3. Ask questions via chat

👉 The system will:

* Break query into sub-parts
* Retrieve relevant context
* Generate refined answer

---

## 🧠 Example

### Input:

```
Compare React vs Angular performance
```

### System Behavior:

* Decomposes query
* Retrieves multiple contexts
* Combines insights

---

## 📈 Why This Project is Strong

This project demonstrates:

* ✅ Multimodal AI
* ✅ RAG system design
* ✅ Agent-based reasoning
* ✅ Real-world pipeline engineering

---

## 💼 Resume Description

> Built a multimodal AI system integrating retrieval-augmented generation, vision models, and agent-based reasoning with query decomposition for improved answer accuracy.

---

## 🔮 Future Improvements

* Add ReAct-style reasoning
* Add answer evaluation agent
* Show reasoning steps in UI
* Add feedback loop

---

## 🏆 Final Note

This is not just a RAG application —
it is a **Multimodal Agentic AI System**, similar to modern research systems used in advanced AI labs.

---
>>>>>>> fdb3fe7 (Initial commit - Multimodal Agentic RAG System)
