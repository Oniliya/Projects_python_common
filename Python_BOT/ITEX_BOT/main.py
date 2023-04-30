from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from aiogram.types import Message

bot = Bot(token='5857170253:AAEsw1Sr-z4ifAMnQ0kkVWyiwUUNVp_8K8Q')
dp = Dispatcher(bot)

async def on_start(_):
    print("БОТ запущен!")

@dp.message_handler(commands=['start'])
async def start_message(message: Message):
    await message.answer('Привет')

@dp.message_handler(commands=['bye'])
async def start_message(message: Message):
    await message.answer('И тебе пока')

@dp.message_handler(commands=['chamomile'])
async def daisy(message: Message):
    data = message.text
    _, number = data.split()
    for i in range (int(number)):
        if i %2:
            await message.answer("Любит")
        else:
            await message.answer("Не любит")



@dp.message_handler()
async def daisy(message: Message):
    await message.answer(message.text)



executor.start_polling(dp, skip_updates=True, on_startup=on_start)


