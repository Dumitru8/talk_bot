import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

token = '5968018051:AAHF6UgH9jItveSlkDT3EAwil6YNcjmROJ8'
openai.api_key = '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'

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler()
async def send(message: types.Message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.9,
        max_tokens=400,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    await message.answer(response['choices'][0]['text'])

executor.start_polling(dp, skip_updates=True)
