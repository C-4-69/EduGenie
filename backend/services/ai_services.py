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