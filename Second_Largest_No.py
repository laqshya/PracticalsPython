print("Enter the numbers and press enter twice to end the list or press any character")
List = []
try:
    while True:
        List.append(int(input()))
except:
    print("second largest number in your List",end=' ')
    List = list(dict.fromkeys(List))
    List.sort()
    print(List[-2])