import os
import openai
from aiogram import Bot, Dispatcher, executor, types

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.reply("🤖 Hi! আমি ChatGPT Bot\nযেকোনো প্রশ্ন করুন")

@dp.message_handler()
async def chat(message: types.Message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message.text}]
        )
        await message.reply(response.choices[0].message.content)
    except:
        await message.reply("⚠️ Error, পরে চেষ্টা করুন")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)