# List comprehension = A concise way to create lists in Python
# Compact and easier to read than traditional loops 
# [expression for value in iterable if condition]

doubles = []
for x in range (1,11):
    doubles.append(x * 2)

print(doubles)

numbers = [1,-2,3,-4,5,-6,8]
# If our value of num meets this condition, simply return it, and place it in num
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]

print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)