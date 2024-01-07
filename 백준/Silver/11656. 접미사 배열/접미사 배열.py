word = input()
a = []
for i in range(len(word)):
    a.append(word[i:])
print(*sorted(a), sep="\n")