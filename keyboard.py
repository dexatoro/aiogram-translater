from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

languages = {'English🇬🇧':'en',
             'Русский🇷🇺':'ru', 
             'Deutsch🇩🇪':'de',
             'Zhōngguó rén🇨🇳':'zh-CN',
             'Nihongo🇯🇵':'ja',
             'Español🇪🇸':'es',}

async def select_language():
    keyboard = ReplyKeyboardBuilder()
    for language in languages:
        keyboard.add(KeyboardButton(text=language))
    return keyboard.adjust(2).as_markup()

# rates = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='English🇬🇧',callback_data='en')],
#     [InlineKeyboardButton(text='Русский🇷🇺',callback_data='ru')],
#     [InlineKeyboardButton(text='Deutsch🇩🇪',callback_data='de')],
#     [InlineKeyboardButton(text='Zhōngguó rén🇨🇳',callback_data='zh')],
#     [InlineKeyboardButton(text='Nihongo🇯🇵',callback_data='ja')],
#     [InlineKeyboardButton(text='Español🇪🇸',callback_data='es')],
# ])