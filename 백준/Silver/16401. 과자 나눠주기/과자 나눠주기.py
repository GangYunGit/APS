import sys

input = sys.stdin.readline
m, n = map(int, input().split())
snack = list(map(int, input().split()))

start, end = 1, max(snack)
result = 0

while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in range(n):
        divide = snack[i] // mid
        if divide > 0:
            count += divide

    if count >= m:
        result = max(mid, result)
        start = mid + 1
    else:
        end = mid - 1

print(result)