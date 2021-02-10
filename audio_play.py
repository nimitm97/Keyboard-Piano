from pydub import AudioSegment
from pydub.playback import play


def play_mp3(audio):
    sound = AudioSegment.from_mp3(audio)
    play(sound)


base_path = "./resources/audios/mp3/"
play_mp3(base_path + "A0.mp3")
