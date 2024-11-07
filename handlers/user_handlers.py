from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from lexicon.lexicon_ru import LEXICON
from keyboards.survey_kb import create_survey_keyboard


router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text=LEXICON[message.text],
        reply_markup=create_survey_keyboard()
    )


# Можно добавить FSM если нужно
@router.callback_query(F.data.in_(['1', '2', '3']))
async def process_low_press(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
        text=LEXICON['low_res_press']
    )
