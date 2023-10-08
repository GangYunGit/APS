m, n = map(int, input().split())
sieve = [False, False] + [True] * (n - 1)
prime = []
for i in range(2, int(n ** 0.5) + 1):
    for j in range(2 * i, n + 1, i):
        if sieve[j]:
            sieve[j] = False

for i in range(m, n + 1):
    if sieve[i]:
        prime.append(i)

print(*prime, sep="\n")