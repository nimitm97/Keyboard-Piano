from os import path
from threading import Thread
from pydub import AudioSegment
from pydub.playback import play


def play_mp3(audio):
    sound = AudioSegment.from_mp3(audio)
    play(sound)


base_path = "./resources/audios/mp3/"
#a_major_chord = play_mp3("A3.mp3") + play_mp3("Db3.mp3") + play_mp3("E3.mp3")
threads = []

threads.append(Thread(target=play_mp3, args=(base_path + "A3.mp3",)))
threads.append(Thread(target=play_mp3, args=(base_path + "Db3.mp3",)))
threads.append(Thread(target=play_mp3, args=(base_path + "E3.mp3",)))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
