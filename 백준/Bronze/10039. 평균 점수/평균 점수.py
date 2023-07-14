a = 0
for _ in range(5):
    b = int(input())
    a += b if b >= 40 else 40
print(a // 5)