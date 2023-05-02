from aiogram.types import Message
from loader import dp


@dp.message_handler(commands=['start'])
async def start_message(message: Message):
    await message.answer(f'{message.from_user.first_name} , Привет')


@dp.message_handler(commands=['bye'])
async def bye_message(message: Message):
    await message.answer('И тебе пока')


@dp.message_handler(commands=['chamomile'])
async def daisy(message: Message):
    data = message.text
    _, number = data.split()
    for i in range(int(number)):
        if i % 2:
            await message.answer("Любит")
        else:
            await message.answer("Не любит")


@dp.message_handler(commands=['ромашка'])
async def daisy(message: Message):
    data = message.text
    _, number = data.split()
    for i in range(int(number)):
        if i % 2:
            await message.answer("Любит")
        else:
            await message.answer("Не любит")


