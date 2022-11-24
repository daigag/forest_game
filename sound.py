import os, time
from pygame import mixer
from gtts import gTTS

mixer.init()

class Read_loud:
    def say(text, filename="temp.mp3", delete_audio_file=True, language="en", slow=False):
        audio = gTTS(text, lang=language, slow=slow)
        audio.save(filename)
        
        mixer.init()
        mixer.music.load(filename)
        mixer.music.play()

        seconds = 0
        while mixer.music.get_busy() == 1:
            time.sleep(0.25)
            seconds += 0.25

        mixer.quit()
        if delete_audio_file:
            os.remove(filename)
