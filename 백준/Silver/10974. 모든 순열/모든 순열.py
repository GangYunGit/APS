def permutaions(nums, end):
    if len(nums) == n:
        print(*nums)
        return

    for i in range(1, end):
        if not used[i]:
            used[i] = True
            nums.append(i)
            permutaions(nums, end)
            used[i] = False
            nums.pop()


n = int(input())
used = [False] * (n + 1)
permutaions([], n + 1)