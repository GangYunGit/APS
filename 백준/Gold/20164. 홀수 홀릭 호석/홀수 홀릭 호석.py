def get_odd(num):
    count = 0
    for i in num:
        if int(i) % 2:
            count += 1
    return count


def dfs(num, count):
    global min_count, max_count
    if len(num) == 1:
        count += get_odd(num)
        min_count = min(count, min_count)
        max_count = max(count, max_count)
        return
    elif len(num) == 2:
        temp1, temp2 = num[0], num[1]
        new_num = int(temp1) + int(temp2)
        dfs(str(new_num), count + get_odd(temp1) + get_odd(temp2))
    else:
        cut_range = len(num)
        for i in range(1, cut_range):
            for j in range(i + 1, cut_range):
                temp1, temp2, temp3 = num[:i], num[i:j], num[j:]
                new_num = int(temp1) + int(temp2) + int(temp3)
                dfs(str(new_num), count + get_odd(temp1) + get_odd(temp2) + get_odd(temp3))


num = input()
min_count = 10 ** 10
max_count = 0
dfs(num, 0)
print(min_count, max_count)