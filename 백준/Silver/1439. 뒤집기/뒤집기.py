s = input()
length = len(s)
count = [0, 0]
for i in range(length):
    if i > 0 and s[i] != s[i - 1]:
        if s[i - 1] == '0':
            count[0] += 1
        else:
            count[1] += 1
    if i == length - 1:
        if s[i] == '0':
            count[0] += 1
        else:
            count[1] += 1
print(min(count))