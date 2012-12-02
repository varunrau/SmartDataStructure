import threading, time
from random import randint
from LiveGraph import *

def main():
  graphThread = LiveGraph()
  graphThread.start()

  while 1:

    ops = randint(0, 100)
    get = randint(0, 100)
    add = randint(0, 100)
    remove = randint(0, 100)
    contains = randint(0, 100)
    time.sleep(0.2)
    
main()




