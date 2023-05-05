import os
import platform
if platform.system() == "Windows":
    command = "PowerShell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{0}')\""
else:
    command = "say '{0}'"
if __name__ == '__main__':
    print("RoboSpeaker 2.0, created by Mohith E.")
    #x="Welcome to RoboSpeaker 2.0, created by Mohith E. My job is to translate what you enter to speech."
    #os.system(command.format(x))
    while True:
        x = input ("Enter what you want to speak: ")
        if x == "q":
            x="bye bye! See you soon!"
            os.system(command.format(x))
            break
        os.system(command.format(x))

