"""
generator.py
"""

from openai import OpenAI

from config import MODEL_NAME
from config import OPENROUTER_API_KEY

from prompts import build_prompt
from router import get_generation_settings

from models import CopyRequest
from models import CopyOutput


client = OpenAI(
  api_key=OPENROUTER_API_KEY,
  base_url="https://openrouter.ai/api/v1",
)


def generate_copy(request: CopyRequest) -> CopyOutput:

    prompt = build_prompt(request)

    settings = get_generation_settings(request.platform)

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        temperature=settings.temperature,
        max_tokens=settings.max_completion_tokens,
    )

    generated_text = response.choices[0].message.content

    return CopyOutput(
        platform=request.platform,
        tone=request.tone,
        copy_text=generated_text,
        word_count=len(generated_text.split()),
    )