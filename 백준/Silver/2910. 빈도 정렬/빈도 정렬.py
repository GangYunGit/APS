from collections import Counter

n, c = map(int, input().split())
nums = list(map(int, input().split()))
counter = Counter([])
for num in nums:
    counter.update({num: 1})

for num, a in counter.most_common():
    for i in range(a):
        print(num, end=" ")