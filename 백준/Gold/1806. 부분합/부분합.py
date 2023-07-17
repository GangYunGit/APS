n, s = map(int, input().split())
num_list = list(map(int, input().split()))

start, end = 0, 0
min_length = 100001
sum_num = 0
num_list_length = 0
while True:
    if start == len(num_list):
        break

    if sum_num >= s:
        min_length = min(num_list_length, min_length)
        sum_num -= num_list[start]
        num_list_length -= 1
        start += 1
        continue

    if end == len(num_list):
        break

    if sum_num < s:
        sum_num += num_list[end]
        num_list_length += 1
        end += 1

if min_length == 100001:
    print(0)
else:
    print(min_length)