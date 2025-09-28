import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

API_TOKEN = '8379999903:AAEnTQqMUPBQ0bjWVw0qkIwZSLNP2FjD9pE'
CHANNEL_ID = '@anarchy_kishfd'

bot = Bot(
    token=API_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

@dp.message(lambda message: message.text)
async def handle_text(message: types.Message):
    await bot.send_message(CHANNEL_ID, message.text)

# Всё остальное игнорируем — без ответа
# (не нужен отдельный хендлер — aiogram сам проигнорирует)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
