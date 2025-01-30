# nested loop = A loop within another loop (outer, inner)
#           outer loop:
#           inner loop:
rows = int(input("Enter the # of rows: "))
cols = int(input("Enter the # of columns: "))
symbol = input("Enter a simbol to use: ")

for x in range (rows):
    for y in range (cols):
        print(symbol, end="")
    print()

