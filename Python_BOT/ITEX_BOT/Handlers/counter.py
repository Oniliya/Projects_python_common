from aiogram.types import Message
from loader import dp
# from Keyboards import keyboard, create_kb, create_kb_counter
# from Keyboards import keyboard, create_kb_counter
from Keyboards import create_kb_counter
from aiogram.dispatcher import filters


import Variables

# @dp.message_handler(commands=['counter'])
@dp.message_handler(filters.Text(contains=Variables.COUNTER))
async def counter_message(message: Message):

    if Variables.BOT_DICT.get(message.from_user.first_name, None):
        Variables.BOT_DICT[message.from_user.first_name] += 1
    else:
        Variables.BOT_DICT[message.from_user.first_name] = 1

    count = Variables.BOT_DICT[message.from_user.first_name]

    print('counter ', Variables.BOT_DICT)

    await message.answer(f'{message.from_user.first_name} , клац клац {count})',
                         reply_markup=create_kb_counter(Variables.COUNTER, count))

