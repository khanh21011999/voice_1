from pydub import AudioSegment
from pydub.silence import split_on_silence
from pydub.silence import detect_nonsilent
import speech_recognition as sr

r = sr.Recognizer()
r.pause_threshold = 5
'''
with sr.Microphone() as source:
    try:
      print("Maximum wait is 2 second")
      audio=r.listen(source,timeout=2)
    except sr.WaitTimeoutError:
        print("waitError")
with open("test1.wav","wb") as f:
    f.write(audio.get_wav_data())
'''
sound = AudioSegment.from_file('thegioi.wav',format="wav")
chucks = split_on_silence(sound,
                          min_silence_len=1000,
                          silence_thresh=-50,
                          keep_silence=1000,
                          seek_step=1)
##print(sound.dBFS)
##print(detect_nonsilent(sound, 1000, -55, 1))
with open('text_document.txt','r',encoding='utf-8') as read_file:
    file=read_file.read()
    print(file)
with open('thegioi.txt','a',encoding='utf-8') as file:
    file.write('https://vnexpress.net/the-gioi/tiem-kich-italy-duoi-theo-may-bay-duc-vi-su-co-mat-lien-lac-3907903.html'+'\n')

for i, chuck in enumerate(chucks):
    out_file = "D:\python_project\XLTN\project_1_XLTN\\thegioi{0}.wav".format(i)
    chuck.export(out_file, bitrate='192k', format="wav")
    filename = 'thegioi'+ str(i) + '.wav'
    file=filename
    with sr.AudioFile(file) as source:
        audio=r.listen(source)
    try:
        rec=r.recognize_google(audio,language='vi-VN')
        with open('thegioi.txt','a',encoding='utf=8') as the_file:

            the_file.write(filename+'\n'+rec+'\n')
    except sr.UnknownValueError:
        print("Could not understand what you said")
    except sr.RequestError as e:
        print("Could not request")