melon = int(input())
ground_info = [list(map(int, input().split())) for _ in range(6)]
small_ground = 0
big_ground = 0

for i in range(6):
    if ground_info[i % 6][0] == 2 and ground_info[(i + 1) % 6][0] == 4:
        small_ground = ground_info[i % 6][1] * ground_info[(i + 1) % 6][1]
        big_ground_idx = [1, 3]
    if ground_info[i % 6][0] == 1 and ground_info[(i + 1) % 6][0] == 3:
        small_ground = ground_info[i % 6][1] * ground_info[(i + 1) % 6][1]
        big_ground_idx = [2, 4]
    if ground_info[i % 6][0] == 4 and ground_info[(i + 1) % 6][0] == 1:
        small_ground = ground_info[i % 6][1] * ground_info[(i + 1) % 6][1]
        big_ground_idx = [2, 3]
    if ground_info[i % 6][0] == 3 and ground_info[(i + 1) % 6][0] == 2:
        small_ground = ground_info[i % 6][1] * ground_info[(i + 1) % 6][1]
        big_ground_idx = [1, 4]

for i in range(6):
    if ground_info[i][0] == big_ground_idx[0]:
        big_ground_1 = ground_info[i][1]
    if ground_info[i][0] == big_ground_idx[1]:
        big_ground_2 = ground_info[i][1]

big_ground = big_ground_1 * big_ground_2
print((big_ground - small_ground) * melon)