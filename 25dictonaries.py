# dictionary = a collection of {key:value} pairs
# ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Bijing",
            "Russia": "Moscow"}

# print(dir(capitals))~
# print(help(capitals))

print(capitals.get("USA"))
print(capitals.get("India"))
print(capitals.get("Russia"))

#if capitals.get("Russia"):
#    print("That capital exists")
#else:
#    print("That capital doesn't exist.")

capitals.update({"Germany":"Berlin"})
capitals.update({"USA": "Ohio"})
capitals.pop("India")
#capitals.popitem()
#capitals.clear()
keys = capitals.keys()
print(keys) 

for key in capitals:
    print(key)

#values = capitals.values()
for value in capitals.values():
    print(value)

items = capitals.items()
print("Items:\n", items)

for key, value in capitals.items():
    print(f"{key}: {value}")
