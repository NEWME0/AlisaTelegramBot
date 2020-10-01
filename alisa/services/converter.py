from pydub import AudioSegment


def convert_ogg_to_wav(ogg_path, wav_path):
    audio = AudioSegment.from_ogg(ogg_path)
    audio.export(wav_path, 'wav')

