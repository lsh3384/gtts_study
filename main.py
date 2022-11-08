from gtts import gTTS
__author__ = 'info-lab'

with open("example.txt", "r", encoding='UTF8') as f:
    txt = f.read()
    # print(f.read())
    print(txt)

    tts = gTTS(
        text=str(txt),
        lang='ko', slow=False
    )
    tts.save('ex_ko.mp3')

    tts1 = gTTS(
        text='Hello',
        lang='en', slow=False
    )
    tts1.save('ex_en.mp3')