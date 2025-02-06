# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#   * unpacking operator
#   1. positional 2. default 3. keyword 4. ARBITRARY

def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(add(5, 15, 1,4))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Mr", "Mahatma", "Gandhi")

# K wargs. We can treat k wargs as a dictionary

def print_address(**kwargs):
    print(type(kwargs))
    #for value in kwargs.values():
    #    print(value)
    #for key in kwargs.keys():
    #    print(key)
    for key, value in kwargs.items():
        print(f"{key}:{value}")

print_address(street="Apple street", city="Tahoma", state="Michigan", zip="1234")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print
    for value in kwargs.values():
        print(value, end= " ")


shipping_label("Dr", "Spongebob", "Squarepants", "III", 
               street="Main street", apt="99",cty="CDMX", ste="Mexico",cp="123")