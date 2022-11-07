# BOJ_1436. 영화감독 숌

idx = int(input())
num_list = []
for i in range(1, 2666800):
    if '666' in str(i):
        num_list.append(i)

print(num_list[idx - 1])
