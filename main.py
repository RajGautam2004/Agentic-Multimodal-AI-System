from fastapi import FastAPI
from pydantic import BaseModel
from rag.enhanced_pipeline import enhanced_rag

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/ask")
def ask_question(req: QueryRequest):
    query = req.query

    response = enhanced_rag(query, retriever, llm)

    return {"response": str(response)}