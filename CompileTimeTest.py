#Compile Time Test
#from time import clock, time
import time, fileinput, string, sys

dataStructures = ["Arr()", "SArr()"]
dataStructureTimes = []

testFileName = "somefile"
testFile = testFileName + ".py"

minTime = sys.maxint

for i in range(len(dataStructures)): #loop through dataStructures
  newFileName = str(testFileName + "_" + dataStructures[i] + ".py")
  file = open(newFileName, "w")

  for line in fileinput.input(testFile): #replace SD() with a d.s.
    line = line.replace("SD()", dataStructures[i])
    file.write(line)
  
  file.close()

  start_time = time.time()
  execfile(newFileName)
  elapsedTime = time.time() - start_time
  dataStructureTimes.append(elapsedTime)

for i in range(len(dataStructures)): 
  print ("Time using %s: %s" % (dataStructures[i], dataStructureTimes[i]))


  


