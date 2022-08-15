# 창고_다각형

import sys

sys.stdin = open('input.txt')

# ---------------------문제 풀이 아이디어---------------------
# 1. 가장 왼쪽부터 시작하여 최대값을 만날 때까지 높이 값을 더해줌
# 2. 현재의 높이보다 큰 값을 만날 때 마다 높이 값을 갱신
# 3. 다시 가장 오른쪽부터 시작하여 최대값을 만날 때까지 높이를 더함
# 4. 2번과 같음

N = int(input())

building_info = [list(map(int, input().split())) for _ in range(N)]
building_info.sort()    # 오름차순 정렬
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

# 반복문의 range를 설정하기 위해 높이의 최대값이 원본 배열의 몇 번째 인덱스인지 구함
for i in building_info:
    for j in range(N):
        if i[1] == max_height:
            max_idx = i[0]

# --가장 왼쪽부터 최대 높이에 도달한 값까지 전부 더함--
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
# ----------------------------------------------------

# --가장 오른쪽부터 최대 높이 직전까지의 값을 전부 더함--
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
# ------------------------------------------------------
print(result)



