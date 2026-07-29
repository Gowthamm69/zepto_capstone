from typing import List
from openai import OpenAI

from config import GROQ_API_KEY, BASE_URL, MODEL_NAME
from prompts import PROMPT_TEMPLATE

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url=BASE_URL
)


def generate_response(question: str, retrieved_docs: List[str], sources: List[str]):

    if not retrieved_docs:
        return {
            "answer": "I couldn't find that information in the available policy documents.",
            "sources": [],
            "confidence": 0.0
        }

    context = "\n\n".join(retrieved_docs)

    prompt = PROMPT_TEMPLATE.format(
        context=context,
        question=question
    )

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful Zepto customer support assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=300
    )

    return {
        "answer": response.choices[0].message.content.strip(),
        "sources": sources,
        "confidence": 1.0
    }