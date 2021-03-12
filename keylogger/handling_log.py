import os

def clear_data():
    username = os.getlogin()
    loggin_directory = f"C:/Users/{username}/log.txt"

    logger_data = open(loggin_directory, 'w')
    logger_data.close