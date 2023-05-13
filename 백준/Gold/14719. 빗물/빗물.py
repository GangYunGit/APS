height, width = map(int, input().split())
world = list(map(int, input().split()))

max_height = 0
max_height_index = 0
result = 0

for i in range(width):
    if world[i] > max_height:
        max_height_index = i
        max_height = world[i]

left_compare = world[0]
right_compare = world[-1]
for i in range(max_height_index):
    if world[i] <= left_compare:
        result += left_compare - world[i]
    else:
        left_compare = world[i]

for i in range(width - 1, max_height_index, -1):
    if world[i] <= right_compare:
        result += right_compare - world[i]
    else:
        right_compare = world[i]
        
print(result)