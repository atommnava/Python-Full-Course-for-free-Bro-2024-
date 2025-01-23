#name = input("Enter your full name: ")
#phone_number = input("Enter your phone nuber: ")
#result = len(name)
#result = name.find(" ")
#result = name.rfind("o")
#name = name.capitalize()
#name = name.upper()
#name = name.lower
#result = name.isdigit() # Returns true or false depending if there are numbers
#result = name.isalpha() # Returns true of false depending if there are no alphabetical numbers like ' '
#result = phone_number.count("-")
#phone_number = phone_number.replace("-", " ")

#print(result)
#print(phone_number)
#print(help(str)) # It shows all of the string methods 

# Validate user input exercise
# 1. Username is no more than 12 characters
# 2. Username must not contain spaces
# 3. Usernme must not contain digits

my_name = input("Enter your username: ")
if len(my_name) > 12:
    print("Your username can't be more than 12 characters")
elif not my_name.find(" ") == -1:
    print("Your usernmae can't contain spaces")
elif not my_name.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {my_name}")