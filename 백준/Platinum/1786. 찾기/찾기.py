t = input()
p = input()
kmp_table = [0 for _ in range(len(p))]
j = 0
for i in range(1, len(p)):
    while j > 0 and p[i] != p[j]:
        j = kmp_table[j - 1]
    if p[i] == p[j]:
        j += 1
        kmp_table[i] = j

find = []
j = 0
for i in range(len(t)):
    while j > 0 and t[i] != p[j]:
        j = kmp_table[j - 1]
    if t[i] == p[j]:
        if j != len(p) - 1:
            j += 1
        else:
            find.append(i - len(p) + 2)
            j = kmp_table[j]
            
print(len(find))
print(*find)