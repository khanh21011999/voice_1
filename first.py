import sounddevice as sd
import soundfile as sf
import time


def record(filename, duration, fs, channels):
    count = 0;
    while count < 2:
        input("press enter to read file")
        path = 'D:\python_project\XLTN\project_1\data\gocnhin\gocnhin_1.txt'
        file = open(path, encoding='utf8')
        contents = file.read()
        print(contents)
        count = count + 1

    '''     
    print('recording')
    my_recording=sd.rec(int(duration*fs),samplerate=fs,channels=channels)
    sd.wait()
    sf.write(filename,my_recording,fs)
    print("done recordin") '''


# playback file
record('new_record.wav', 10, 16000, 1)
