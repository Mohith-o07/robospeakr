from gtts import gTTS
import os
if __name__=='__main__':
    print("Welcome to RoboSpeaker 1.0, created by Mohith E")
    while True:
        mytext=input("enter your text:")
        ending_note="bye bye, take care Soldier"
        if mytext=='x':
            audio=gTTS(text=ending_note,lang="en",slow=False)
            audio.save("example.mp3")
            os.system("start example.mp3")
            break
        audio=gTTS(text=mytext,lang="en",slow=False)
        audio.save("example.mp3")
        os.system("start example.mp3")
