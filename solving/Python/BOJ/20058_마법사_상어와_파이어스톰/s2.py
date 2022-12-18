a = [[1, 2], [3, 4]]
b = list(zip(*a[::-1]))

print(a[::-1])
print(b)