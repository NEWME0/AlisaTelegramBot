import os
import subprocess


SERVICE_DIR = os.path.dirname(os.path.abspath(__file__))

FFMPEG = os.path.join(SERVICE_DIR, 'bin/ffmpeg.exe')

if not os.path.isfile(FFMPEG):
    raise Exception(f'FFmpeg not found at {FFMPEG}')


devnull = open(os.devnull, 'w')


def convert_audio(source_file: str, destination_file: str) -> None:
    command_line_args = [FFMPEG, '-i', source_file, destination_file]
    return_code = subprocess.call(command_line_args, stdout=devnull, stderr=devnull)

    if return_code != 0:
        raise Exception(f"FFmpeg exit with error code {return_code}")
