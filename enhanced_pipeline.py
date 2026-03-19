# rag/enhanced_pipeline.py

from agents.planner import plan_and_execute

def enhanced_rag(query, retriever, llm):
    return plan_and_execute(query, retriever, llm)