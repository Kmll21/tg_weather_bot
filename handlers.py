from aiogram import Router
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