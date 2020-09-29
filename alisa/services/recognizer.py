from io import BytesIO
from typing import Union

from speech_recognition import *


recognizer = Recognizer()


def audio_file_to_text(audio_file: Union[BytesIO, str], language: str = 'ru-RU') -> str:
    with AudioFile(audio_file) as audio_file_io:
        audio_data = recognizer.record(source=audio_file_io)
        return recognizer.recognize_google(audio_data, language=language)
