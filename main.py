import pyautogui, time, \
pystray, threading, os, sys, \
win32api, win32process, win32con
from random import randrange
from PIL import Image, ImageDraw

def set_high_priority():
    handle = win32api.OpenProcess(
        win32con.PROCESS_ALL_ACCESS, True, os.getpid()
        )
    
    win32process.SetPriorityClass(
        handle, win32process.HIGH_PRIORITY_CLASS
        ) # can be set to REALTIME_PRIORITY_CLASS etc.

set_high_priority()

class Class_Run_States:
    def __init__(self):
        self.__running = False
        self.__stop_event = threading.Event()
        
    def run(self):
        while not self.__stop_event.is_set():
            pyautogui.moveRel(1, 0, duration = 0)       # 1 and -1 are coordinates of the coursor,
            pyautogui.moveRel(-1,0, duration = 0)       # can be set to 0 but after that
            time.sleep(randrange(3, 25))                # you can't see whether the app run or not
            print('running')
                
    def change_running_state(self):
        print(f'Running: {self.__running}')
        self.__running = not self.__running
        print(f'Running: {self.__running}')
        
        if self.__running:
            self.__stop_event.clear()
            t = threading.Thread(target=self.run)
            t.start()
        else:
            self.__stop_event.set()

if __name__ == '__main__':
    
    def resource_path(relative_path):
        try:
            # Creating a temp folder and storing path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath('.')

        return os.path.join(base_path, relative_path)
    
    def start(icon, item):
            print('start')
            crs.change_running_state()

    def stop(icon, item):
        print('stop')
        crs.change_running_state()

    def exit_program(icon, item):
        print('exit')
        crs.change_running_state()
        icon.stop()
        os._exit(1)
    
    def create_image(width, height, color1, color2):
        image = Image.new('RGB', (width, height), color1)
        dc = ImageDraw.Draw(image)
        dc.rectangle(
            (width // 2, 0, width, height // 2),
            fill=color2)
        dc.rectangle(
            (0, height // 2, width // 2, height),
            fill=color2)
        return image

    # image = Image.open(resource_path('Image/touchpad.ico'))   # If you wanna use your own icon
                                                                # you need to hide/remove above 'create_image' function
    crs = Class_Run_States()
    icon = pystray.Icon('Rectangles', icon = create_image(64, 64, 'black', 'white'))
    # icon = pystray.Icon('touchpad', image)                    # and activate what's hidden under comments
    icon.menu=pystray.Menu(
        pystray.MenuItem('Start', start),
        pystray.MenuItem('Stop', stop),
        pystray.MenuItem('Exit', exit_program),
    )

    icon.run_detached()
