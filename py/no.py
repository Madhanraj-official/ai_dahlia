import pyaudio
from vosk import Model,KaldiRecognizer

print('lisen')
modal = Model("/home/gokul/py/vosk-model-small-en-in-0.4")
recognizer=KaldiRecognizer(modal,16000)
mic = pyaudio.PyAudio()
stream=mic.open(format=pyaudio.paInt16,channels=1,rate=16000,input=True,frames_per_buffer=8192)
stream.start_stream()
while True:
    data = stream.read(4096)
    if recognizer.AcceptWaveform(data):
        print(recognizer.Result())
        

