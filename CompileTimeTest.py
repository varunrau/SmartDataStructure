#Compile Time Test
from time import clock, time
import fileinput, string

dataStructures = ["Arr()", "SArr()"]

testFileName = "somefile"
testFile = testFileName + ".py"



for i in range(len(dataStructures)): #loop through dataStructures
  newFileName = str(testFileName + "_" + dataStructures[i] + ".py")
  file = open(newFileName, "w")

  for line in fileinput.input(testFile): #replace SD() with a d.s.
    line = line.replace("SD()", dataStructures[i]);
    file.write(line)

  start_time = time()
  print "New file name: %s" % newFileName
  execfile(str(newFileName));
  print str(time() - start_time) + " " + "seconds\n"

  file.close



