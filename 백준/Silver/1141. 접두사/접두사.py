n = int(input())
words = sorted([input() for _ in range(n)], key=lambda x: len(x))
s = set()
for word in words:
    for i in range(len(word)):
        check = word[:i + 1]
        if check in s:
            s.remove(check)
            s.add(word)
            break
    else:
        s.add(word)
print(len(s))