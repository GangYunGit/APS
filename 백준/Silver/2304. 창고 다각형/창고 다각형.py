N = int(input())

building_info = [list(map(int, input().split())) for _ in range(N)]
building_info.sort()
left_list = []
height_list = []
result = 0
max_idx = 0

for i in building_info:
    left_list.append(i[0])
    height_list.append(i[1])

left = min(left_list)
right = max(left_list)


max_height = max(height_list)

for i in building_info:
    for j in range(N):
        if i[1] == max_height:
            max_idx = i[0]
            
new_height = 0
new_left = 0
j = 0
for i in range(left, max_idx + 1):
    if left_list[j] == i:
        if height_list[j] > new_height:
            new_height = height_list[j]
            j += 1
        else:
            j += 1
    result += new_height

new_height = 0
new_left = 0
j = N - 1
for i in range(right, max_idx, -1):
    if left_list[j] == i:
        if height_list[j] > new_height:
            new_height = height_list[j]
            j -= 1
        else:
            j -= 1
    result += new_height

print(result)