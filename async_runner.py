"""
async_runner.py
"""

import asyncio
from prompts import build_prompt
from router import get_generation_settings
from openai import AsyncOpenAI

from config import (
  
  
    MODEL_NAME,
    OPENROUTER_API_KEY,
    MAX_CONCURRENT_REQUESTS
)



from models import (

    CopyRequest,
    CopyOutput
)


client = AsyncOpenAI(
    api_key=OPENROUTER_API_KEY
)

semaphore = asyncio.Semaphore(
    MAX_CONCURRENT_REQUESTS
)


async def generate_async(
    request: CopyRequest
) -> CopyOutput:

    async with semaphore:

        prompt = build_prompt(request)

        settings = get_generation_settings(
            request.platform
        )

        response = await client.chat.completions.create(
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

        text = response.choices[0].message.content

        return CopyOutput(
            platform=request.platform,
            tone=request.tone,
            copy_text=text,
            word_count=len(text.split())
        )
    

    
async def generate_many(
    requests: list[CopyRequest]
) -> list[CopyOutput]:

    tasks = [

        generate_async(r)

        for r in requests

    ]

    return await asyncio.gather(
        *tasks
    )

