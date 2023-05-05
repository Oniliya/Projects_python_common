from aiogram.types import Message
from loader import dp
from aiogram.dispatcher.filters import Filter, Text
from aiogram.dispatcher import filters
from Keyboards import create_kb_counter


@dp.message_handler(filters.Text(contains='phone'))
async def get_phone(message: Message):
    await message.answer(f'{message.from_user.first_name} , номер телефона !!!!!!!')
    # await message.answer(f'{message.from_user.first_name} , номер телефона !!!!!!!',reply_markup=)

    # await message.answer(f'{message.from_user.first_name} , Не могу - не помогу!  ', reply_markup=keyboard())