# BOJ_15686. 치킨 배달


def combinations(start, end):
    if len(picked_bbq) == end:
        bbq_points.append(picked_bbq[:])
        return

    for i in range(start, len(bbq_list)):
        picked_bbq.append(bbq_list[i])
        combinations(i + 1, end)
        picked_bbq.pop()


def m_distance(bbq_point):
    global min_distance
    chicken_distance = 0
    for i in range(city_size):
        for j in range(city_size):
            if city_info[i][j] == 1:
                distance_list = []
                for (bbq_i, bbq_j) in bbq_point:
                    m_d = abs(bbq_i - i) + abs(bbq_j - j)
                    distance_list.append(m_d)
                chicken_distance += min(distance_list)
                if chicken_distance > min_distance:
                    break

    if chicken_distance < min_distance:
        min_distance = chicken_distance


city_size, alive_BBQ = map(int, input().split())
city_info = [list(map(int, input().split())) for _ in range(city_size)]
bbq_list = []
picked_bbq = []
bbq_points = []
min_distance = 100 * 13

for i in range(city_size):
    for j in range(city_size):
        if city_info[i][j] == 2:
            bbq_list.append((i, j))

combinations(start=0, end=alive_BBQ)

for bbq_point in bbq_points:
     m_distance(bbq_point)

print(min_distance)
