from aiogram.utils import executor

# from Handlers.handlers import dp
from Handlers import dp

from Database import create_users_table

from Database import DataBase

db = DataBase()
db.find_user('users', name='STONE', age=38, city="KRD")





async def on_start(_):
    print('Database ....', end='')
    try:
        create_users_table()
        print("...OK!")
    except:
        print("...FAILURE!")

    print("БОТ запущен!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_start)
