import time
import logging

logging.basicConfig(filename='/var/log/visum.log', level=logging.DEBUG)

if __name__ == '__main__':
    while True:
        logging.info('boot task is running')
        time.sleep(5)
