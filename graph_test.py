import threading, time
from random import randint
import LiveGraph
import globalz

def main():
  graphThread = LiveGraph.LiveGraph()
  graphThread.start()

  while 1:

    globalz.num_ops = randint(0, 100)
    globalz.switch_ds_toggle = randint(0,20)
    globalz.which = randint(0,5)
    
    globalz.contains_ctr = randint(0, 100)
    globalz.add_ctr = randint(0, 100)
    globalz.remove_ctr = randint(0, 100)
    globalz.get_ctr = randint(0, 100)
     
    time.sleep(0.2)
    
main()




