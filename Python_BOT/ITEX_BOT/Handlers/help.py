from aiogram.types import Message
from loader import dp
from Keyboards import keyboard, create_kb

@dp.message_handler(commands=['help'])
async def help_message(message: Message):
    await message.answer(f'{message.from_user.first_name} , Не могу - не помогу!  ', reply_markup=create_kb())

