# BOJ_1676. 팩토리얼 0의 개수

n = int(input())
count_2 = 0
count_5 = 0
for i in range(1, n + 1):
    while not i % 2:
        if i % 2 == 0:
            count_2 += 1
            i //= 2

    while not i % 5:
        if i % 5 == 0:
            count_5 += 1
            i //= 5

print(min(count_2, count_5))