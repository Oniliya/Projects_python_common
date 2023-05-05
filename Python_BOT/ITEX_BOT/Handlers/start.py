from aiogram.types import Message
from loader import dp
from Keyboards import create_kb_counter
import Variables


@dp.message_handler(commands=['start'])
async def start_message(message: Message):
    if Variables.BOT_DICT.get(message.from_user.first_name, None):
        # Variables.BOT_DICT[message.from_user.first_name] = 0
        count = Variables.BOT_DICT[message.from_user.first_name]
    else:
        count = 0

    await message.answer(f'{message.from_user.first_name} , Привет',
                         reply_markup=create_kb_counter(Variables.COUNTER, count))


@dp.message_handler(commands=['bye'])
async def bye_message(message: Message):
    if Variables.BOT_DICT.get(message.from_user.first_name, None):
        # Variables.BOT_DICT[message.from_user.first_name] = 0
        count = Variables.BOT_DICT[message.from_user.first_name]
    else:
        count = 0

    await message.answer(f'И тебе пока, {message.from_user.first_name}',
                         reply_markup=create_kb_counter(Variables.COUNTER, count))


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


