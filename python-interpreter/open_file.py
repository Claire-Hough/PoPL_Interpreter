import sys
from my_parser import *
import os


def begin(filename):
    # if len(args) == 1:
    #     print args[0]
    fd = os.open(filename, os.O_RDONLY, '0777')
    contents = ''
    while True:
        buf = os.read(fd, 16)
        contents += buf
        if buf == '':
            # we're done
            break
    contents = contents


if __name__ == '__main__':
    
    begin('test.py')