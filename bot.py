# bot.py
import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import main as main_handlers

# Создаём бота и диспетчер
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Подключаем роутеры (хендлеры)
dp.include_router(main_handlers.router)

async def main():
    print("🤖 Бот запущен.")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())