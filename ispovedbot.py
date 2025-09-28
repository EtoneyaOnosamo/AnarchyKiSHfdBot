import os
import asyncio
from aiogram import Bot, Dispatcher, types

# Берём токен из переменной окружения
TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TOKEN:
    raise ValueError("Не найден токен бота. Установи TELEGRAM_TOKEN в переменных окружения.")

# Создаём объекты бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Пример команды /start
@dp.message()
async def cmd_start(message: types.Message):
    await message.answer("Бот работает!")

# Пример функции отправки сообщения в канал
async def send_message_to_channel(text: str):
    channel_id = "@anarchy_kishfd"  # Замени на свой канал
    await bot.send_message(chat_id=channel_id, text=text)

async def main():
    # Запуск polling
    try:
        print("Бот стартовал...")
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
