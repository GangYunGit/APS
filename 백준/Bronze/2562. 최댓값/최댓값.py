nums = []
for _ in range(9):
    nums.append(int(input()))
max_num = max(nums)
print(max_num)
for i in range(9):
    if nums[i] == max_num:
        print(i + 1)
        break