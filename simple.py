"""Build a simple LLM Application"""

import os
import groq
from dotenv import load_dotenv
load_dotenv()


GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
groq_client = groq.Groq(api_key = GROQ_API_KEY)

sys_prompt = """You are a helpful assistant. Your goal is to provide useful and relevant responses to my request"""

models = [
    "llama-3.1-405b-reasoning",
    "llama-3.1-70b-versatile",
    "llama-3.1-8b-instant",
    "mixtral-8x7b-32768"
]


def generate(models, query, temperature=0.1):
    response = groq_client.chat.completions.create(
        model = models,
        messages = [
            {"role": "system", "content": sys_prompt},
            {"role": "system", "content": query},
        ],
        response_format = {"type": "text"},
        temperature = temperature
    )

    answer = response.choices[0].message.content

    return answer

if __name__ == "__main__":
    model = models[1]
    query = "which is bigger 9.9 or 9.11"
    response = generate(model, query, temperature=0)
    print(response)



