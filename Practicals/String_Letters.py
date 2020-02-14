Letters = 26
Str1 = "Lakshya".lower()
Str2 = "Yashdeep".lower()

Hash_table = [0] * Letters

for i in range(len(Str1)) :
    Hash_table[ord(Str1[i]) - ord('a')] = 1

for  i in range(len(Str2)) :
    if Hash_table[ord(Str2[i]) - ord('a')] == 1 or Hash_table[ord(Str2[i]) - ord('a')] == -1:
        Hash_table[ord(Str2[i]) - ord('a')] = -1
    else:
        Hash_table[ord(Str2[i]) - ord('a')] = 2

for i in  range(0,Letters):
    if Hash_table[i] == 1 or Hash_table[i] == 2 :
        print(chr(i + ord('a')))