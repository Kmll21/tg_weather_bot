import time

from aiogram import Router, F
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import Command
from sqlalchemy.orm import Session

from parse import parse_weather
from database.database import engine
from database.models import Weather


router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    menu = ReplyKeyboardMarkup(
        keyboard=[KeyboardButton(text="⛅ Узнать погоду", callback_data="weather")],
        resize_keyboard=True
    )
    await msg.answer(f"Привет, {msg.from_user.full_name}! Я помогу тебе узнать текущую погоду в твоём городе. Введи название своего города", reply_markup=menu)


@router.message(F.text.lower() == "⛅ узнать погоду")
async def get_weather(msg: Message):
    with Session(engine) as session:
        current_city = session.query(Weather).filter(Weather.user_id == msg.from_user.id).first()

        if current_city:
            await msg.answer(parse_weather(current_city.city))
        else:
            await msg.answer("Город не выбран")


@router.message(Command("c"))
async def change_city(msg: Message):
    name = " ".join(msg.text.split(" ")[1:])
    response = parse_weather(name)

    if response != "Некорректное название города":
        with Session(engine) as session:
            current_city = session.query(Weather).filter(Weather.user_id == msg.from_user.id).first()
            current_city.city = name
            session.commit()
        await msg.answer("Успешно!")
        await msg.answer(response)
    else:
        await msg.answer("Некорректное название города")


@router.message()
async def message_handler(msg: Message):
    time.sleep(1)
    with Session(engine) as session:
        current_city = session.query(Weather).filter(Weather.user_id == msg.from_user.id).first()
        if current_city:
            await msg.answer(parse_weather(msg.text))
        else:
            new_city = Weather(
                user_id=msg.from_user.id,
                city=msg.text
            )
            response = parse_weather(msg.text)

            if response != "Некорректное название города":
                session.add(new_city)
                session.commit()

            await msg.answer(response)