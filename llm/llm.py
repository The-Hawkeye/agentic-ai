from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_answer(context, question):

    prompt = f"""
    Use the context below to answer the question.

    Context:
    {context}

    Question:
    {question}

    Answer clearly and concisely.
    """

    response = client.chat.completions.create(
        # model="llama3-8b-8192",
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content