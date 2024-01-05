a = []
for _ in range(5):
    a.append(int(input()))
print(min([a[0] + a[3], a[0] + a[4], a[1] + a[3], a[1] + a[4], a[2] + a[3], a[2] + a[4]]) - 50)