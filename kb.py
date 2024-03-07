from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu = ReplyKeyboardMarkup(
    keyboard=[
    [KeyboardButton(text="⛅ Узнать погоду", callback_data="check_weather")],
    [KeyboardButton(text="📍 Изменить свой город", callback_data="change_city")],
    ],
    resize_keyboard=True
)