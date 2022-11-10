#code to take screenshot in linux
import pyautogui
import os
import logging
import logging.handlers
import time

#logging.basicConfig(filename='screenshot.log',level=logging.DEBUG)
logger = logging.getLogger('screenshot')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.handlers.RotatingFileHandler('screenshot.log', maxBytes=1000000, backupCount=5)
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)  

# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

current_time = None

#take screenshot
def take_screenshot():
    time.sleep(10)
    logger.info('Taking screenshot')
    #get current time
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    pyautogui.screenshot('./shots/{}_.png'.format(current_time))
    logger.info('Screenshot taken')

#check if screenshot exists
def check_screenshot():
    logger.info('Checking if screenshot exists')
    if os.path.isfile('{}_.png'.format(current_time)):
        logger.info('Screenshot exists')
        return True
    else:
        logger.info('Screenshot does not exist')
        return False

if __name__ == '__main__':
    # take_screenshot()
    #take screenshot every 10 seconds
    while True:
        if not check_screenshot():
            take_screenshot()
        else:
            logger.error('Screenshot already exists')
        time.sleep(10)