import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import CommandStart
dp = Dispatcher()

# Создаем класс StatesGroup для состояний
class LanguageChoice(StatesGroup):
    choice = State()

# ReplyKeyboardMarkup для выбора языка
select_language = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='English🇬🇧')],
    [KeyboardButton(text='Deutsch🇩🇪')],
    [KeyboardButton(text='Русский🇷🇺')],
    [KeyboardButton(text='Zhōngguó rén🇨🇳')],
    [KeyboardButton(text='Nihongo🇯🇵')],
    [KeyboardButton(text='Español🇪🇸')],
    ],
    resize_keyboard=True,
    input_field_placeholder='На какой язык переводить?'
)

# Обработчик команды /start
@dp.message(CommandStart)
async def start(message: types.Message):
    await message.answer("Выберите язык", reply_markup=select_language)
    await LanguageChoice.choice.set()

# Обработчик выбора языка пользователя
@dp.message(state=LanguageChoice.choice)
async def process_choice(message: types.Message, state: FSMContext):
    chosen_language = message.text
    if chosen_language == 'English🇬🇧':
        # Устанавливаем переменную для английского языка
        await state.update_data(language='english')
    elif chosen_language == 'Deutsch🇩🇪':
        # Устанавливаем переменную для немецкого языка
        await state.update_data(language='german')
    # Добавьте обработку для остальных языков
    await message.answer(f"Вы выбрали язык: {chosen_language}")
    await state.finish()

async def main() -> None:
    bot = Bot(token="7197430463:AAGOGdzw7NeIrbRRz-TxHcwr2RLVqAlcpyk")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')
