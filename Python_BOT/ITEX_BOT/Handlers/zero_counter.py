from aiogram.types import Message
from loader import dp

from Keyboards import create_kb_counter
from aiogram.dispatcher import filters

import Variables

@dp.message_handler(commands=['zero'])
async def zero_message(message: Message):

    if Variables.BOT_DICT.get(message.from_user.first_name, None):
        Variables.BOT_DICT[message.from_user.first_name] = 0
    else:
        Variables.BOT_DICT[message.from_user.first_name] = 0

    print('zero ',Variables.BOT_DICT)
    await message.answer(f'{message.from_user.first_name} , обнулилось!! :)',
                         reply_markup=create_kb_counter(Variables.COUNTER, 0))


