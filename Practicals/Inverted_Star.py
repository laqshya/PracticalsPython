lines = int(input("Enter the number of lines"))

for i in range(lines, 0, -1):
    print((lines-i) * " " + "*" * i)