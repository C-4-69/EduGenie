from fastapi import FastAPI
from services.ai_services import ask_ai

app = FastAPI(title="EduGenie")


@app.get("/")
def root():
    return {"message": "Welcome to EduGenie"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/ask")
def ask(question: str):
    answer = ask_ai(question)
    return {
        "question": question,
        "answer": answer
    }