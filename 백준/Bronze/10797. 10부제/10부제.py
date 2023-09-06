a = int(input())
nums = list(map(int, input().split()))
count = 0
for num in nums:
    if num == a:
        count += 1
print(count)