# BOJ_2440. 별 찍기-3

star_list = ['*' * i for i in range(1, 101)]
N = int(input())
for i in range(N - 1, -1, -1):
    print(star_list[i])
