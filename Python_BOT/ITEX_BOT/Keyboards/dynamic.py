from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

switch = 'ON'


def create_kb(name: str) -> ReplyKeyboardMarkup:
    global switch

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    if switch == "ON":
        switch = 'OFF'
    else:
        switch = 'ON'

    btn_start = KeyboardButton(text='/start')
    btn_help = KeyboardButton(text='/help')
    btn_name = KeyboardButton(text=name)

    btn_switch = KeyboardButton(text=switch)

    # btn_loca = KeyboardButton(text='GEO', request_location=True)
    # btn_phone = KeyboardButton(text='PHONE', request_contact=True)

    keyboard.add(btn_start, btn_help, btn_name, btn_switch)

    return
