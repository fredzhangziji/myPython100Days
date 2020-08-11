from random import randint
from time import time, sleep
from multiprocessing import Process
from os import getpid


def download_file(filename):
    print('Downloading process initiating. PID: %d.' % getpid())
    print('downloading %s ...' % filename)
    time_to_download = randint(1,5)
    sleep(time_to_download)
    print('%s successfully downloaded! Time taken: %d' % (filename, time_to_download))


def main():
    start = time()
    p1 = Process(target=download_file, args=('Python_self_learning.pdf',))
    p1.start()
    p2 = Process(target=download_file, args=('hahaha.avi',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('Total time taken: %d' % (end - start))

if __name__ == "__main__":
    main()