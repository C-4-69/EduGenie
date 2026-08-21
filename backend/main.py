from fastapi import FastAPI
from services.ai_services import ask_ai
from services.ai_services import explain_topic

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

@app.get("/explain")
def explain(topic: str):
    explanation = explain_topic(topic)
    return {
        "topic": topic,
        "explanation": explanation
    }