N = int(input())
work_hours = [list(map(int, input().split())) for _ in range(N)]

work_hours.sort(key=lambda x : (x[1], x[0]))

next_dock = work_hours[0][1]
count = 1
for i in range(1, N):
    if work_hours[i][0] >= next_dock:
        count += 1
        next_dock = work_hours[i][1]

print(count)