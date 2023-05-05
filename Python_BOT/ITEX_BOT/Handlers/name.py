# from aiogram.types import Message
# from loader import dp
# # from Keyboards import keyboard, create_kb, create_kb_counter
# # from Keyboards import keyboard, create_kb_counter
# from Keyboards import create_kb_counter
#
# count = 0
#
#
# @dp.message_handler(commands=['counter'])
# async def name_message(message: Message):
#     global count
#     # name = message.from_user.first_name + str(count)
#     # name = message.from_user.first_name
#     name = 'counter '
#     count += 1
#     # await message.answer(f'{message.from_user.first_name} , клац клац ', str(count),
#     #                          reply_markup=create_kb_counter(name, count))
#     await message.answer(f'{message.from_user.first_name} , клац клац + {count})', reply_markup=create_kb_counter(name, count))
#
#
