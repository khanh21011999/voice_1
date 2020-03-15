from pydub import AudioSegment
from pydub.silence import split_on_silence
import speech_recognition as sr
import os
import wavio

sound = AudioSegment.from_wav('tbn.wav')
r = sr.Recognizer()

chucks = split_on_silence(sound,
                          min_silence_len=400,
                          silence_thresh=-40)
print(sound.dBFS)
for i, chuck in enumerate(chucks):
    out_file = "D:\python_project\XLTN\project_1\data\gocnhin\chuck{0}.wav".format(i)
    chuck.export(out_file, bitrate='192k', format="wav")
    filename = 'chuck' + str(i) + '.wav'
    file=filename
    with sr.AudioFile(file) as source:
        audio=r.listen(source)
    try:
        rec=r.recognize_google(audio,language='vi-VN')
        with open('test.txt','a',encoding='utf=8') as the_file:

            the_file.write(filename+'\n'+rec+'\n')
    except sr.UnknownValueError:
        print("Could not understand what you said")
    except sr.RequestError as e:
        print("Could not request")
