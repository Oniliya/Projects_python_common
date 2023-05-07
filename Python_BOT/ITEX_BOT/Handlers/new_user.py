from aiogram.types import Message
from loader import dp
from aiogram.dispatcher.filters import Text
# from Database import new_user, get_login_password
from Database import get_login_password


# from Database import DataBase, new_user


# @dp.message_handler(Text(contains='создать', ignore_case=True))
# async def add_new_user(message: Message):
#     # await message.answer('')
#     name = message.from_user.first_name
#     tg_id = message.from_user.id
#
#     # создать stone 1234 qwer
#     _, login, password = message.text.split()
#
#     params = (name, tg_id, login, password)
#     new_user(params)
#     await message.answer('Добавил пользователя')


@dp.message_handler(commands=['login'])
async def check_user(message: Message):
    _, login, password = message.text.split()
    # print(_,'|', login, '|', password)
    tg_id = message.from_user.id

    # true_log, true_pass = get_login_password(tg_id)
    # print(true_log,'|', true_pass)
    # _, login, password = message.text.split()

    for pair in get_login_password(tg_id):
        if pair[0] == login and pair[1] == password:
            await message.answer('авторизация прошла успешно')
            break
    else:
        await message.answer('неверный логин или пароль')

    # if true_log == login and true_pass == password:
    #     await message.answer('авторизация прошла успешно')
    # else:
    #     await message.answer('неверный логин или пароль')
