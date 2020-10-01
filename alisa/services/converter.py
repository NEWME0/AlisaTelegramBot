from pydub import AudioSegment


def convert_ogg_to_wav(ogg_path: str, wav_path: str) -> None:
    audio = AudioSegment.from_ogg(ogg_path)
    audio.export(wav_path, 'wav')

