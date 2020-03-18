from pydub import AudioSegment
from pydub.silence import split_on_silence
import speech_recognition as sr
r = sr.Recognizer()
r.pause_threshold=5
with sr.Microphone() as source:
    print("taliking after 2 second(stop talking for 5 sec to stop and save)")
    audio=r.listen(source,timeout=2)
    print(r.recognize_google(audio,language='vi-VN'))
with open("test1.wav","wb") as f:
    f.write(audio.get_wav_data())
sound = AudioSegment.from_wav('test1.wav')
chucks = split_on_silence(sound,
                          min_silence_len=500,
                          silence_thresh=-45)
print(sound.dBFS)
for i, chuck in enumerate(chucks):
    out_file = "D:\python_project\XLTN\project_1\\thoi_su\chuck{0}.wav".format(i)
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
