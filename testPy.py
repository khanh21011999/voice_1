from pydub import AudioSegment
from pydub.silence import split_on_silence
#from pydub.silence import detect_nonsilent
import speech_recognition as sr
import soundfile as sf
import sounddevice as sd
import sys
import queue
from sounddevice import default
import numpy
assert numpy
##record audio tham khảo tại https://github.com/spatialaudio/python-sounddevice/blob/master/examples/rec_unlimited.py
q = queue.Queue()
with open('text_document.txt', 'r', encoding='utf-8') as read_file:
    file = read_file.read()
    print(file)
filename = 'thogioi6.wav'
samplerate = 44100
def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy())


try:
    with sf.SoundFile(filename, mode='x', samplerate=samplerate, channels=1) as soundFlie:
        with sd.InputStream(samplerate=samplerate, device=default.device, channels=1, callback=callback):
            print('>>>>>>press Ctrl+C to stop<<<<<<<')
            while True:
                soundFlie.write(q.get())
except KeyboardInterrupt:
    print('\n Recorded '+repr(filename))
r = sr.Recognizer()
'''
r.pause_threshold = 5 ## thời gian ngưng nhận âm tối đa để dừng
with sr.Microphone() as source:
    try:
      print("Maximum wait is 2 second")
      audio=r.listen(source,timeout=2)  ##timeout thời gian đợi bắt đầu nói tối đa
    except sr.WaitTimeoutError:
        print("waitError")
with open("test1.wav","wb") as f:
    f.write(audio.get_wav_data())
'''
sound = AudioSegment.from_file(filename, format="wav")
chucks = split_on_silence(sound,
                          min_silence_len=1000,  # thời gian được xem là im lặng để phân tách câu
                          silence_thresh=-50,  ##ngưỡng im lặng được xem là im lặng (đơn vị dBFS)
                          keep_silence=1000,  ##khoang im lặng sau khi tách câu phát âm
                          seek_step=1)
print(sound.dBFS)
##print(detect_nonsilent(sound, 1000, -55, 1))

with open('thegioi.txt', 'a', encoding='utf-8') as file:
    file.write('https://vnexpress.net/the-gioi/tiem-kich-italy-duoi-theo-may-bay-duc-vi-su-co-mat-lien-lac-3907903.html' + '\n')
for i, chuck in enumerate(chucks):
    out_file = "D:\python_project\XLTN\project_1_XLTN\\thegioi{0}.wav".format(i)
    chuck.export(out_file, bitrate='192k', format="wav")
    filename = 'thegioi' + str(i) + '.wav'
    file = filename
    with sr.AudioFile(file) as source:
        audio = r.listen(source)
    try:
        rec = r.recognize_google(audio, language='vi-VN')
        with open('thegioi.txt', 'a', encoding='utf=8') as the_file:

            the_file.write(filename + '\n' + rec + '\n')
    except sr.UnknownValueError:
        print("Could not understand what you said")
    except sr.RequestError as e:
        print("Could not request")
