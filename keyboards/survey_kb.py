from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def create_survey_keyboard(unique_id: int) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()

    # Добавляем первый ряд (1, 2, 3, 4, 5)
    kb_builder.row(
        InlineKeyboardButton(text='1', callback_data=f"rate_{unique_id}_1"),
        InlineKeyboardButton(text='2', callback_data=f"rate_{unique_id}_2"),
        InlineKeyboardButton(text='3', callback_data=f"rate_{unique_id}_3"),
        InlineKeyboardButton(text='4', callback_data=f"rate_{unique_id}_4"),
        InlineKeyboardButton(text='5', callback_data=f"rate_{unique_id}_5")
    )

    # Добавляем второй ряд (6, 7, 8, 9, 10)
    kb_builder.row(
        InlineKeyboardButton(text='6', callback_data=f"rate_{unique_id}_6"),
        InlineKeyboardButton(text='7', callback_data=f"rate_{unique_id}_7"),
        InlineKeyboardButton(text='8', callback_data=f"rate_{unique_id}_8"),
        InlineKeyboardButton(text='9', callback_data=f"rate_{unique_id}_9"),
        InlineKeyboardButton(text='10', callback_data=f"rate_{unique_id}_10")
    )

    return kb_builder.as_markup()
