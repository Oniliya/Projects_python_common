from aiogram.utils import executor

# from Handlers.handlers import dp
from Handlers import dp


async def on_start(_):
    print("БОТ запущен!")




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_start)
