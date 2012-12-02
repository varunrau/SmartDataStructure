#Compile Time Test
from time import clock, time

def main():
  print "hi"


start_time = time()
main()
print str(time() - start_time) + " seconds"
