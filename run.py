import asyncio
import logging
from os import getenv
from deep_translator import GoogleTranslator
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from keyboard import select_language, languages

TOKEN = getenv("TOKEN")

# Определение состояний
class UserState(StatesGroup):
    lang = State()

# Создание хранилища для состояний
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await message.answer(f"Hello, {message.from_user.full_name}!\nSelect the language to translate into\n(default=Русский)", reply_markup= await select_language())
    await state.set_state(UserState.lang)

@dp.message(lambda message: message.text in languages)
async def dest_lang(message: Message, state: FSMContext):
    await state.update_data(lang=languages[message.text])
    await message.reply(f'{message.text} selected')

@dp.message()
async def echo_handler(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    lang = data.get('lang', 'ru')  # Если язык не установлен, по умолчанию используется 'ru'
    try:
        translated_text = GoogleTranslator(source='auto', target=lang).translate(message.text)
        await message.answer(translated_text)
    except TypeError:
        await message.answer("Nice try!")

async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')
