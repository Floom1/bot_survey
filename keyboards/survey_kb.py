from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon_ru import LEXICON


def create_survey_keyboard(unique_id: int) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    for i in range(1, 11):
        kb_builder.row(
        InlineKeyboardButton(
            text=str(i),
            callback_data=f"rate_{unique_id}_{i}"
        )
        )
    return kb_builder.as_markup()
