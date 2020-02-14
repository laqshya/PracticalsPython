print("Enter the numbers and press enter twice to end the list or press any character")
List = []
try:
    while True:
        List.append(int(input()))
except:
    print("Maximum number in your List",end=' ')
    print(max(List))