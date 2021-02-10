import keyboard
from pydub import AudioSegment
from pydub.playback import play


def play_mp3(audio):
    sound = AudioSegment.from_mp3(audio)
    play(sound)


def key_hook(event):
    while event.name == 'a':
        while keyboard.is_pressed('a'):
            play_mp3(base_path + "A3.mp3")


base_path = "./resources/audios/mp3/"

# if keyboard.is_pressed('f'):
#    play_mp3(base_path + "A3.mp3")

keyboard.hook(key_hook)
keyboard.wait('Esc')
