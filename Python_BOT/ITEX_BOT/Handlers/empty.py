from aiogram.types import Message
from loader import dp



@dp.message_handler()
async def daisy(message: Message):
    await message.answer(f'{message.from_user.first_name}, смотри, что нашел - {message.text}')


