a = []
for _ in range(7):
    i = int(input())
    if i % 2:
        a.append(i)
if not a:
    print(-1)
else:
    print(sum(a))
    print(min(a))