from services.generator import generate_business_idea
from services.visuals import generate_image
from services.smm import generate_instagram_posts
from utils.pdf import create_post_pdf
from aiogram.types import FSInputFile

@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("🧠 Генерирую бизнес-идею...")
    idea = generate_business_idea()

    await message.answer("✍️ Генерирую 3 варианта постов...")
    posts = generate_instagram_posts(idea)

    await message.answer("🖼 Создаю визуал...")
    image_url = generate_image(idea)

    # Отправим визуал
    await message.answer_photo(photo=image_url, caption="Вот ваш визуал к идее 📸")

    # Отправим посты как текст
    for i, post in enumerate(posts, 1):
        await message.answer(f"<b>Пост {i}:</b>\n\n{post}", parse_mode="HTML")

    # PDF
    pdf_path = create_post_pdf(posts)
    pdf_file = FSInputFile(path=pdf_path, filename="Nurox_Posts.pdf")
    await message.answer_document(pdf_file, caption="📄 Все посты в PDF-файле")
