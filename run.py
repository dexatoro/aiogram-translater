import asyncio
import logging
from os import getenv
from deep_translator import GoogleTranslator
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from keyboard import select_language, languages

lang = 'ru'
TOKEN = getenv("TOKEN")

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {message.from_user.full_name}!\nSelect the language to translate into\n(default=Русский)", reply_markup= await select_language())

@dp.message(lambda message: message.text=='English🇬🇧' or message.text=='Deutsch🇩🇪' or
                    message.text=='Русский🇷🇺' or message.text=='Español🇪🇸' or
                    message.text=='Zhōngguó rén🇨🇳' or message.text=='Nihongo🇯🇵')
async def dest_lang(message: Message):
    global lang
    lang=languages[message.text]
    await message.reply(f'{message.text} selected')    

@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.answer(GoogleTranslator(source='auto', target=lang).translate(message.text))
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