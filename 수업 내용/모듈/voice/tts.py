import imp
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

file_path = 'tts.txt'

with open(file_path, 'rt', encoding='UTF8') as f:
    read_file = f.read()

# text = "요 크크 나는 윤영"

tts = gTTS(text = read_file, lang = 'el')

mp = ('hhhi.mp3')

tts.save(mp)


# mp3 재생
playsound(mp)