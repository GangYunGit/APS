# BOJ_1182. 부분수열의 합


def combinations(num_list, start):
    global count

    if pick and sum(pick) == sum_nums:
        print(pick)
        count += 1

    for i in range(start, nums):
        if not used[i]:
            used[i] = True
            pick.append(num_list[i])
            combinations(num_list, start + 1)
            pick.pop()
            used[i] = False


nums, sum_nums = map(int, input().split())
num_list = list(map(int, input().split()))


used = [False for _ in range(nums)]
pick = []
result = []
count = 0
combinations(num_list, 0)

print(count)