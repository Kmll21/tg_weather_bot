from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
kb = [
    [KeyboardButton(text="⛅ Узнать погоду", callback_data="check_weather")],
    [KeyboardButton(text="📍 Изменить свой город", callback_data="change_city")],
]

# menu = ReplyKeyboardMarkup(
menu = ReplyKeyboardMarkup(
    keyboard=kb,
    resize_keyboard=True
)
# exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
# iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])