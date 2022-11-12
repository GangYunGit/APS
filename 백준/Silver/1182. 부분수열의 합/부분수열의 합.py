def combinations(index, start):
    global count

    if index >= nums:
        return

    start += num_list[index]
    if start == sum_nums:
        count += 1

    combinations(index + 1, start - num_list[index])
    combinations(index + 1, start)


nums, sum_nums = map(int, input().split())
num_list = list(map(int, input().split()))


used = [False for _ in range(nums)]
pick = []
result = []
count = 0
combinations(index=0, start=0)

print(count)