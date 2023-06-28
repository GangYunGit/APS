goal_ch = int(input())
n = int(input())
broken_list = []
if n:
    broken_list = list(map(str, input().split()))

gap = abs(goal_ch - 100)

for i in range(1000001):
    for num in str(i):
        if num in broken_list:
            break
    else:
        gap = min(gap, abs(i - goal_ch) + len(str(i)))
print(gap)
