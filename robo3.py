import win32com.client as wincom
speak=wincom.Dispatch("SAPI.SpVoice")
if __name__ == '__main__':
    print("RoboSpeaker 3.0, created by Mohith E.")
    while True:
        x = input("Enter what you want to speak: ")
        if x == "q":
            x="Bye bye! See you soon!"
            speak.Speak(x)
            break
        speak.Speak(x)