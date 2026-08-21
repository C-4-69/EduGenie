import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def ask_ai(question: str) -> str:
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=f"""
You are EduGenie, an educational AI assistant.

Answer the student's question clearly and accurately.
Use simple language and provide useful educational context.

Student question:
{question}
"""
    )

    return response.text


def explain_topic(topic: str) -> str:
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=f"""
You are EduGenie, an educational AI assistant.

Explain the following topic to a student in very simple language.
Use:
- A simple definition
- An intuitive explanation
- A real-world example
- Key points to remember

Topic:
{topic}
"""
    )

    return response.text

def generate_quiz(topic: str) -> str:
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=f"""
You are EduGenie, an educational AI assistant.

Create a short quiz about the following topic.

Generate exactly 5 multiple-choice questions.

For each question provide:
1. The question
2. Four options labeled A, B, C, D
3. The correct answer
4. A one-sentence explanation

Topic:
{topic}
"""
    )

    return response.text