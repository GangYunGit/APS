# BOJ_20058_마법사 상어와 파이어스톰

ice_size, casting = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(2 ** ice_size)]
power_list = list(map(int, input().split()))

for power in power_list:
    divide = (2 ** ice_size) // (2 ** power)
    new_ice = [[] for _ in range(2 ** ice_size)]
    for i in range(divide):
        for j in range(divide):
            storm = [[] for _ in range(2 ** power)]
            for r_i in range(2 ** power):
                for r_j in range(2 ** power):
                    storm[r_i].append(ice[i * 2 ** power + r_i][j * 2 ** power + r_j])
            rotated_storm = list(map(list, zip(*storm[::-1])))
            print(rotated_storm)
        for k in range(2 ** power):
            new_ice[i * 2 ** power + k].append(rotated_storm[i * 2 ** power])
    print(new_ice)



