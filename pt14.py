print("Program to print start pattern: \n");

rows = input("Enter max star to be display on single line")
rows = int (rows)
for i in range (0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range (rows, 0, -1):
    for j in range(0, i -1):
        print("*", end=' ')
    print("\r")