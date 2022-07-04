from gtts import gTTS

def speak(st):
    tts = gTTS(text=st, lang="en")
    filename = "test.mp3"
    tts.save(filename)

speak("안녕하세요")