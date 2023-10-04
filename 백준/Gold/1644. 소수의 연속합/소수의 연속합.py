import sys
input = sys.stdin.readline


n = int(input())

sieve = [True] * (n + 1)
for i in range(2, int(n ** 0.5) + 1):
    for j in range(i * 2, n + 1, i):
        if sieve[j]:
            sieve[j] = False

prime_list = [2]
for i in range(3, n + 1):
    if sieve[i]:
        prime_list.append(i)

prime_sum = prime_list[0]
count = 0
start, end = 0, 0

while True:
    if end > len(prime_list):
        break

    if prime_sum <= n:
        end += 1
        if prime_sum == n:
            count += 1
        if end >= len(prime_list):
            break
        prime_sum += prime_list[end]
    else:
        prime_sum -= prime_list[start]
        start += 1

print(count)