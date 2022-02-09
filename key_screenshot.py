import keyboard,os,getpass
from PIL import ImageGrab
import datetime,time

path = os.path.join('C:\\','Users',getpass.getuser(),'Documents','LazyScreenShots/')
if not os.path.exists(path):
    os.makedirs(path)


while True:
    current_time = datetime.datetime.now().strftime("%d-%H-%M-%S-%MS")
    try:
        if keyboard.is_pressed('0+-'):
            img = ImageGrab.grab()
            img.save(f'{path}ScreenShot-{current_time}.png')
            time.sleep(1)
        elif keyboard.is_pressed('0+*'):
            break
    except Exception as e:
        print(e)