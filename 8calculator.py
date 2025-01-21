# Python calculator

operator = input("Enter an operator (+ - / *): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if (operator == "+"):
    print(f"Sum is {num1 + num2}")

elif (operator == "-"):
    print(f"Subtractions is {num1 - num2}")

elif (operator == "/"):
    print(f"Division is {num1 / num2}")

elif (operator == "*"):
    print(f"Multiplication is {num1 * num2}")

else:
    print(f"{operator} is not valid")
