# BOJ_1182. 부분수열의 합


def combinations(num_list, start):
    global count

    if pick and sum(pick) == 0:
        count += 1

    for i in range(start, nums):
        if not pick or num_list[i] >= max(pick):
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
count = 0
combinations(num_list, 0)
print(count)