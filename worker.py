import time
from datetime import datetime


def main():
    while True:
        print("Datetime: " + str(datetime.now()))
        time.sleep(60)


main()
