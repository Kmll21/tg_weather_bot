from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from sqlalchemy.orm import Session

import kb
from parse import parse_weather
from database.database import engine
from database.models import Weather


router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(f"Привет, {msg.from_user.full_name}! Я помогу тебе узнать текущую погоду в твоём городе. Введи название своего города", reply_markup=kb.menu)


@router.message(F.text.lower() == "⛅ узнать погоду")
async def get_weather(msg: Message):
    with Session(engine) as session:
        current_city = session.query(Weather).filter(Weather.user_id == msg.from_user.id).first()

        if current_city:
            await msg.answer(parse_weather(current_city.city))
        else:
            await msg.answer("Город не выбран")


@router.message(F.text.lower() == "📍 изменить свой город")
async def change_city(msg: Message):
    await msg.answer("Введите название города")
    response = parse_weather(msg.text)

    if response != "Некорректное название города":
        with Session(engine) as session:
            city = session.query(Weather).filter(Weather.user_id == msg.from_user.id).first()
            city.city = msg.text
            session.commit()
    else:
        await msg.answer("Некорректное название города")
    await msg.answer()


@router.message()
async def message_handler(msg: Message):
    with Session(engine) as session:
        current_city = session.query(Weather).filter(Weather.user_id == msg.from_user.id).first()
        if current_city:
            await msg.answer(f"Город уже выбран: {current_city.city}")
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