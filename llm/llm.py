from groq import Groq
import os

client = Groq(api_key=os.environ["GROQ_API_KEY"])


def generate_answer(context, question):

    prompt = f"""
You are a helpful assistant.

Context:
{context}

Question:
{question}

Answer clearly and concisely.
"""

    response = client.chat.completions.create(
        # model="llama3-70b-8192",
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content