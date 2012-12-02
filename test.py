# Test File

from main import *

s_data = SD()

for x in range(10):
   s_data.add(x)

print(str(s_data.contains(3)) + " should be true")

s_data.remove(3)
print(str(s_data.contains(3)) + " should be false")

print(str(s_data.get(0)) + " should be 0")

