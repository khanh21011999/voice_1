from pydub import AudioSegment
from pydub.silence import split_on_silence
from pydub.silence import detect_nonsilent
import speech_recognition as sr

r = sr.Recognizer()
r.pause_threshold = 3
'''
with sr.Microphone() as source:
    try:
      print("taliking after 2 second")
      audio=r.listen(source,timeout=2)
      print(r.recognize_google(audio,language='vi-VN'))
    except sr.WaitTimeoutError:
        print("waitError")
with open("test1.wav","wb") as f:
    f.write(audio.get_wav_data())
'''
sound = AudioSegment.from_file('untitled.wav',format="wav")
chucks = split_on_silence(sound,
                          min_silence_len=1000,
                          silence_thresh=-54,
                          keep_silence=0,
                          seek_step=1)
print(sound.dBFS)
print(detect_nonsilent(sound, 1000, -54, 1))



'''
for i, chuck in enumerate(chucks):
    out_file = "D:\python_project\XLTN\project_1\\thoi_su\chuck{0}.wav".format(i)
    chuck.export(out_file, bitrate='192k', format="wav")
    filename = 'chuck' + str(i) + '.wav'
    file=filename
    with sr.AudioFile(file) as source:
        audio=r.listen(source)
    try:
        rec=r.recognize_google(audio,language='vi-VN')
        with open('thoisu.txt','a',encoding='utf=8') as the_file:

            the_file.write(filename+'\n'+rec+'\n')
    except sr.UnknownValueError:
        print("Could not understand what you said")
    except sr.RequestError as e:
        print("Could not request")
'''