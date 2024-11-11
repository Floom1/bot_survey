from aiogram import Router, F
from aiogram.filters import Command, CommandObject
from aiogram.types import Message, CallbackQuery

import requests

from database.work_db import add_rating
from filters.filter_employee import IsEmployeeFilter
from services.generate_id import generate_unique_id
from lexicon.lexicon_ru import LEXICON
from keyboards.survey_kb import create_survey_keyboard


router = Router()


@router.message(Command("start"))
async def process_start_command(message: Message, command: CommandObject):
    args = command.args
    if not args.isdigit():
        await message.answer("Неверный ID встречи.")
        return

    unique_id = int(args)

    await message.answer(
        text=LEXICON['/start'],
        reply_markup=create_survey_keyboard(unique_id)
    )


# Можно добавить FSM если нужно
# @router.callback_query(F.data.in_(['1', '2', '3']))
# async def process_low_press(callback: CallbackQuery):
#     await callback.message.delete()
#     await callback.message.answer(
#         text=LEXICON['low_res_press']
#     )


@router.message(Command("gen_qr"), IsEmployeeFilter())
async def generate_qr_code_handler(message: Message):
    unique_id = generate_unique_id()
    qr_url = f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=t.me/fit_sport1_bot?start={unique_id}"

    try:
        response = requests.get(qr_url)
        if response.status_code == 200:
            await message.answer_photo(photo=response.url, caption="Вот ваш QR-код")
        else:
            await message.answer("Ошибка при создании QR-кода. Пожалуйста, попробуйте позже.")
    except requests.exceptions.RequestException:
        await message.answer("Ошибка соединения с сервером QR-кодов.")


@router.callback_query(F.data.startswith("rate_"))
async def process_rating(callback: CallbackQuery):
    # Извлекаем ID встречи и оценку из callback_data
    _, unique_id, rate = callback.data.split("_")
    unique_id = int(unique_id)
    rate = int(rate)

    # Добавляем запись в базу данных
    add_rating(unique_id, rate)

    # Удаляем сообщение с клавиатурой и благодарим пользователя за оценку
    await callback.message.delete()
    await callback.message.answer("Спасибо за вашу оценку!")

    await callback.answer()