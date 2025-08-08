import json
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
ipdb_key = os.getenv("IPDB")
openai_key = os.getenv("OPENKEY001")
# org = os.getenv("OPENORG")  # optional, for organization arg if needed
client = OpenAI(api_key=openai_key)


async def analyze_dream(message: str) -> dict:
    prompt = f"""
    You are an AI dream analyzer. The following information
    is the transcript of a person explaining a dream they recently had.
    As a dream analyzer, it is your responsibility to analyze the dream,
    and explain to this person what it might mean.

    Please return the explanation as a json object matching this schema:
    {{
        "message": {message},
        "analysis": "your analysis goes here..."
    }}

    Dream transcript:
    {message}
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return json.loads(response.choices[0].message.content.strip())
    except Exception as e:
        return {"error": str(e)}
