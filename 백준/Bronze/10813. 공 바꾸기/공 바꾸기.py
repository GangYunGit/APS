n, m = map(int, input().split())
basket = [i for i in range(1, n + 1)]
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    basket[a], basket[b] = basket[b], basket[a]
print(*basket)