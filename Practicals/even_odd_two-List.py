l = [12, 13, 14, 15]
even = []
odd = []
even = list(filter(lambda x: x % 2 == 0, l))
odd = list(filter(lambda x: x % 2 != 0, l))
print(even)
print(odd)