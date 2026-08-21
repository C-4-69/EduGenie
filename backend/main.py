from fastapi import FastAPI
from services.ai_services import (
    ask_ai,
    explain_topic,
    generate_quiz,
    summarize_text
)

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

@app.get("/quiz")
def quiz(topic: str):
    quiz_data = generate_quiz(topic)
    return {
        "topic": topic,
        "quiz": quiz_data
    }

@app.get("/summarize")
def summarize(text: str):
    summary = summarize_text(text)
    return {
        "summary": summary
    }