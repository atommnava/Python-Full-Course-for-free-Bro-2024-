# function = A block of reusable code
#   Place () after the function name to invoke it.

def happy_birthday(name, age):
    print(f"Happy Birthday {name}, you are {age} years old!")

for i in range(0, 3):
    happy_birthday("Atom", 20)

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("BroCode", 42.50, "2025/02/04")

# Return statement
def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

print("result is: ", add(1, 11))

z = subtract(13, 2)
print("subtract result is: ", z)

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("Elon", "Musk")
print(f"Your full name is {full_name}!")