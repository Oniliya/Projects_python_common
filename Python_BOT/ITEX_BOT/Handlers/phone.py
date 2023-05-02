from aiogram.types import Message
from loader import dp
from aiogram.dispatcher.filters import Filter, Text


@dp.message_handler(text=['PHONE'])
async def get_phone(message: Message):
    await message.answer(f'{message.from_user.first_name} , номер телефона !!!!!!!')
