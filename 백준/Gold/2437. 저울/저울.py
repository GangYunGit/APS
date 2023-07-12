n = int(input())
weight_list = list(map(int, input().split()))
weight_list.sort()
temp = 0
for i in range(len(weight_list)):
    if temp + 1 >= weight_list[i]:
        temp += weight_list[i]
    else:
        break
print(temp + 1)