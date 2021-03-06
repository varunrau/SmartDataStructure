#Compile Time Test
#from time import clock, time
import time, fileinput, string, sys, operator, os
from DS import *

#dataStructures = ["Arr()", "SArr()"]
dataStructures = range(DS.NUM_STRUCTURES)
dataStructureTimes = []

testFileName = "test_compile"
testFile = testFileName + ".py"

minTime = sys.maxint

for i in range(len(dataStructures)): #loop through dataStructures
  newFileName = str(testFileName + "_T" + str(dataStructures[i]) + ".py")
  file = open(newFileName, "w")

  for line in fileinput.input(testFile): #replace SD() with a d.s.
    line = line.replace("SD()", "SD(True, " + str(dataStructures[i]) + ")")
    file.write(line)

  file.close()

  start_time = time.time()
  execfile(newFileName)
  elapsedTime = time.time() - start_time
  dataStructureTimes.append(elapsedTime)

for i in range(len(dataStructures)): #print times
  print ("Time using %s: %s" % (dataStructures[i], dataStructureTimes[i]))

minIndex, minValue = min(enumerate(dataStructureTimes), key=operator.itemgetter(1))

print "Fastest is %d" % (minIndex)

#create *_optimized.py with SD set to False
file = open(testFileName + "_optimized.py", "w")
fastestFileName = str(testFileName + "_T" + str(minIndex) + ".py")

for line in fileinput.input(fastestFileName):
  line = line.replace("SD(True", "SD(False")
  file.write(line)

file.close()

#remove temp testing files
for filename in os.listdir("."):
  if filename.startswith(testFileName + "_T"):
    os.remove(filename)














