import math

print (math.pi)

friends = 0
friends = friends+1 # The same
friends+=1 # The same
friends-=2
friends += 1
friends *= 5
friends /= 5
friends =  friends ** 2 # To the power of 'n'
remainder = 1
remainder %= 1

print("Remainder is ", remainder)

x = 3.14
y = 4
z = 5

#result = round(x)
#result = abs(y)
#result = pow(4,3)
#result = math.sqrt(x)
#result math.ceil(x) value goes up
result = math.floor(x)  #value goes down

print("Result is ", result)

mx = max(x,y,z)
print("Max value is ", mx)

radius = float(input("Enter the raidus of the circle: "))
circumference = 2 * math.pi * radius
print(f"The circumference is: {round(circumference, 2)}") # Second arg is for rounding decimal values

a = float(input("Enter side A:"))
b = float(input("Enter side B:"))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"Side C = {c}")




