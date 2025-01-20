name = "Atom"
age = 25
gpa = 3.2
is_student = True

print(type(name))

gpa = int(gpa)
print(gpa)

age = str(age)
print(age)

print(type(age))

name1 = input("Name: ")
age1 = input("Age: ")

print(f"Hello {name1}!")
print(f"You are {age1} yeasrs old")

# Exercise 1 Rectangle Area Calc

length = float(input("Enter the lenght: "))
width = float(input("Enter the width: "))
area = length * width
print("Area is ", area)
print(f"Area is {area}")

# Exercise 2 Shopping cart program

item = input("What item would you like to buy?")
price = float(input("What is the price?"))
quantity = int(input("How many would you like?"))
total = price * quantity
print(f"You have bought {quantity} x {item}/s")
print(f"Your total is {total}")
