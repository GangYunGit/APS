# BOJ_2156. 포도주 시식
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def dfs(start, drink, continue_drinking):
    global max_drink

    if drink > max_drink:
        max_drink = drink

    if start >= n:
        return

    remain_wine = sum(wine_list[start:])
    if drink + remain_wine <= max_drink:
        return

    for i in range(start, n):
        drink += wine_list[i]
        continue_drinking += 1
        print(i, drink, continue_drinking)
        if continue_drinking == 2:
            continue_drinking = 0
            dfs(i + 2, drink, continue_drinking)
            drink -= wine_list[i]
            continue_drinking = 0
        else:
            dfs(i + 1, drink, continue_drinking)
            drink -= wine_list[i]
            continue_drinking -= 1


n = int(input())
wine_list = [int(input()) for _ in range(n)]
max_drink = 0

dfs(start=0, drink=0, continue_drinking=0)

print(max_drink)
