from aiogram import Bot, Dispatcher, types
from app.utils.config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я твой новый бот.")

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply("Отправь мне что-нибудь, и я отвечу!")

# Добавь здесь больше обработчиков...

if __name__ == "__main__":
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
