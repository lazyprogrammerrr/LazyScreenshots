#IMPORTING MODULES

import sys,os
import speech_recognition as sr
import pyttsx3
import pyautogui
import datetime,time,getpass

listner = sr.Recognizer()   #INSTANCE OF RECOGNIZER

engine = pyttsx3.init()     #INIT TEXT TO SPEECH

# THIS FUNCTION WILL TAKE SCREENSHOT COMMAND
def take_command():
    global current_time
    global command
    current_time = datetime.datetime.now().strftime("%d-%H-%M-%S-%MS")      #CAPTURING CURRENT TIME FOR IMAGE NAME
    try:
        with sr.Microphone() as source:                                     #TURNING ON MIC
            print("Listening")
            voice = listner.listen(source)                                  #AS METHOD SAYS 'LISTEN' THIS WILL LISTEN TO YOUR VOICE
            command = listner.recognize_google(voice)                       #USING GOOGLE VOICE API
            command = command.lower()
            if 'screenshot' in command:
                print(command)
                screen_shot()                                               #SCREENSHOT FUNCTION
                engine.say("Screenshot Taken")
                engine.runAndWait()
    except Exception as e:
        print(e)
        
#DIRECTORY FOR SAVING THE IMAGES
path = os.path.join('C:\\','Users',getpass.getuser(),'Documents','LazyScreenShots/')
if not os.path.exists(path):
    os.makedirs(path)

#SCREENSHOT FUNCTION
def screen_shot():
    img = pyautogui.screenshot()                                           #THIS METHOD WILL CAPTURE THE SCREENSHOT
    img.save(f'{path}{current_time}.png')                                  #SAVING IMAGE

username = getpass.getuser()

#INFINE LOOP UNTIL YOU SAY "BYE"
while True:
    take_command()
    time.sleep(0.5)
    if 'bye' in command:
        print(command)
        engine.say(f"Bye {str(username)}")
        engine.runAndWait()
        sys.exit()