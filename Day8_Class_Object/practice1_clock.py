'''
Create a clock with Class and Object.
    1/3/2020
    written by Fred Zhang
'''

from time import sleep
import os

class clock(object):

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour   # make this protected
        self._minute = minute
        self._second = second
    
    def run(self):
        self._second += 1   # every second, _second increases by 1
        # when _second reach 60 seconds, reset and _minute increases by 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            # when _minute reaches 60 minutes, reset and _hour increases by 1
            if self._minute == 60:
                self._hour += 1
                self._minute = 0
                # when _hour reaches 24 hours, reset _hour
                if self._hour == 24:
                    self._hour = 0
    
    def currentTime(self):
        os.system('clear')  # clear the output
        # print the new current time
        print('%.2d:%.2d:%.2d' % (self._hour, self._minute, self._second))
    
def main():
    print("Initiating the clock...")
    # create the object clock1
    clock1 = clock(23,59,50)
    while True:
        clock1.run()
        clock1.currentTime()
        sleep(1)    # after 1 second

if __name__ == '__main__':
    main()
        