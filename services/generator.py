# services/generator.py
import os
from openai import AsyncOpenAI

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def generate_business_idea():
    prompt = (
        "Ты — инновационный AI-кофаундер. "
        "Придумай свежую, прибыльную и технологичную бизнес-идею: краткое описание, целевая аудитория, монетизация, УТП."
    )

    response = await client.chat.completions.create(
        model="gpt-4o",  # или gpt-4 / gpt-3.5-turbo
        messages=[
            {"role": "system", "content": "Ты опытный AI-кофаундер, помогающий запускать успешные стартапы."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.85,
        max_tokens=600
    )

    return response.choices[0].message.content.strip()