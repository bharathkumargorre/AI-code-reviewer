import os
import json
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env
load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def review_code(code: str):
    prompt = f"""
You are a senior software engineer.

Analyze the following code and return ONLY valid JSON.

Format:

{{
    "bugs": "",
    "security": "",
    "performance": "",
    "best_practices": "",
    "quality_score": 0
}}

Code:

{code}
"""

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="llama-3.3-70b-versatile"
    )

    response_text = response.choices[0].message.content

    try:
        return json.loads(response_text)

    except json.JSONDecodeError:
        return {
            "bugs": "Unable to parse AI response",
            "security": "Unable to parse AI response",
            "performance": "Unable to parse AI response",
            "best_practices": response_text,
            "quality_score": 0
        }