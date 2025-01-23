# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a condition
#                          if condition else Y.

num = 5
a = 6
b = 7
age = 25
temperature = 20
user_role = "guest"
#print("Positive " if num > 0 else "Negative")
#result = "EVEN" if num % 2 == 0 else "ODD"
max_num = a if a > b else b # Return a if a > b, else return b
min_num = a if a < b else b
status = "Adult" if age >= 18 else "CHILD"
weather = "HOT" if temperature > 20 else "COLD"
access_level = "FULL Access" if user_role == "admin" else "Limited access"
#print(result)
#print(min_num)
#print(status)
#print(weather)
print(access_level)