# collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits_list = ["apple", "orange", "banana", "coconut"]
print(fruits_list)
# print(fruits_list[::2]) # I would like every second element
                        #       ['apple', 'banana']
                        #       Beggining from index zero

print("pineapple" in fruits_list) # False
fruits_list[0] = "atoms_apple"
fruits_list.remove("atoms_apple")

for x in fruits_list:
    print(x)

# SETS
clothes_set = {"Jacket", "T-shirt", "Socks", "Socks"}

# print(clothes_set[0]) ERROR: Set is unordered
clothes_set.add("Gloves")
print(clothes_set)


# TUPLES
food_list = ("cake", "cookies", "bread")
print(food_list)
print(food_list[0])
print(food_list.index("cake"))