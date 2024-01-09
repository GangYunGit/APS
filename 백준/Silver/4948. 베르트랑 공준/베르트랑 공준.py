while True:
    n = int(input())
    if n == 0:
        break
    sieve = [False] * 2 * (n + 1)
    for i in range(2, int((2 * n) ** 0.5) + 1):
        for j in range(2 * i, 2 * n + 1, i):
            if not sieve[j]:
                sieve[j] = True
    num = []
    for i in range(n + 1, 2 * n + 1):
        if not sieve[i]:
            num.append(i)
    print(len(num))