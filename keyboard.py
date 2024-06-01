from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

select_language = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='English🇬🇧')],
    [KeyboardButton(text='Deutsch🇩🇪')],
    [KeyboardButton(text='Русский🇷🇺')],
    [KeyboardButton(text='Zhōngguó rén🇨🇳')],
    [KeyboardButton(text='Nihongo🇯🇵')],
    [KeyboardButton(text='Español🇪🇸')],
    ],
                                 resize_keyboard=True,
                                 input_field_placeholder='На какой язык переводить?')