count = 0
nums = list(map(int, input().split()))
for num in nums:
    if num > 0:
        count += 1
print(count)