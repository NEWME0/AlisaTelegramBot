from aiogram import *
from aiogram.types import *

from .services.storage import generate_unique_destinations
from .services.converter import convert_ogg_to_wav
from .services.recognizer import audio_file_to_text
from .services.assistant import dispatch_query

from .settings import API_TOKEN


bot = Bot(token=API_TOKEN)
dispatcher = Dispatcher(bot)


@dispatcher.message_handler(commands=['start'])
async def welcome(message: Message) -> None:
    answer = 'Привет! \n' \
             'Меня зовут Алиса \n' \
             'Я умею распозновать речь. \n'
    await message.answer(answer)


@dispatcher.message_handler(content_types=ContentType.VOICE)
async def assist(message: Message) -> None:
    ogg_destination, wav_destination = generate_unique_destinations()
    await message.voice.download(destination=ogg_destination)
    convert_ogg_to_wav(ogg_destination, wav_destination)
    query = audio_file_to_text(wav_destination)
    answer = dispatch_query(query, message)
    await message.delete()
    await message.answer(answer)


@dispatcher.message_handler()
async def echo(message: Message) -> None:
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)
