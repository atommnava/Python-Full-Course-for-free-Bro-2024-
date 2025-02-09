
# module = a file containing code you want to include in your program
# use 'import' to include a module (built-in or your own) 
# useful to break up a large program reusable separate files
# import math
# import math as m
# from math import e
import math
import modulesptii

print(help("modules"))
#print(math.pi)
#print(e.pi)
#print(e)

a, b, c, d, e = 1, 2, 3, 4, 5
print(math.e ** a)
print(math.e ** b)
print(math.e ** c)
print(math.e ** d)

# Thechnically what we've done is we have created another version of 'e'
# We will end up using the second version rahter than the version
# that we have imported from the math module
print(math.e ** e)

result = modulesptii.pi
result = modulesptii.square(3)
result = modulesptii.cube(3)
result = modulesptii.circumference(3)
result = modulesptii.area(3)

print(result)