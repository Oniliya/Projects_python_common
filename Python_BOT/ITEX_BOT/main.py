from aiogram.utils import executor

# from Handlers.handlers import dp
from Handlers import dp

from Database import create_users_table


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
