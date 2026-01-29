from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Legal Document Q&A System (RAG)")

# Request model
class QueryRequest(BaseModel):
    question: str

# Placeholder route
@app.post("/ask")
def ask_question(request: QueryRequest):
    """
    Placeholder endpoint for answering questions from documents.
    Currently returns the same question as a response.
    """
    return {
        "question_received": request.question,
        "answer": "This is a placeholder answer. Integration with LLM will be added here."
    }

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the Legal Document Q&A System (RAG) API"}
