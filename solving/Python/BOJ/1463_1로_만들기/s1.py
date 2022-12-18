# BOJ_1463. 1로 만들기

num_list = [0 for _ in range(10 ** 6 * 3 + 1)]

for i in range(1, 10 ** 6 + 1):
    if num_list[i + 1] == 0 or num_list[i] + 1 < num_list[i + 1]:
        num_list[i + 1] = num_list[i] + 1
    if num_list[i * 2] == 0 or num_list[i] + 1 < num_list[i * 2]:
        num_list[i * 2] = num_list[i] + 1
    if num_list[i * 3] == 0 or num_list[i] + 1 < num_list[i * 3]:
        num_list[i * 3] = num_list[i] + 1

idx = int(input())
print(num_list[idx])
