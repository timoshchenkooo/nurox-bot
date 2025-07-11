import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_instagram_posts(idea: str, count: int = 3) -> list[str]:
    prompt = (
        "Ты — профессиональный копирайтер и маркетолог.\n"
        f"Создай {count} разных вариантов Instagram-постов для бизнес-идеи:\n\n"
        f"«{idea}»\n\n"
        "Каждый пост должен включать:\n"
        "1. Заголовок\n"
        "2. 2 абзаца основного текста\n"
        "3. Призыв к действию\n"
        "4. 5-7 хештегов\n\n"
        "Посты должны быть живыми, понятными, на русском языке. Раздели каждый пост с помощью '###'."
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.85,
            max_tokens=1500
        )
        all_text = response.choices[0].message.content
        return [post.strip() for post in all_text.split("###") if post.strip()]
    except Exception as e:
        return [f"⚠️ Ошибка при генерации постов: {e}"]
