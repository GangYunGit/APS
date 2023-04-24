di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def dfs(set_obstacle):
    global students, result
    if set_obstacle == 3:
        avoid_count = 0
        # print(room)
        for i, j in student_points:
            if check_student(i, j):
                avoid_count += 1

        if avoid_count == students:
            result = "YES"
        set_obstacle -= 1
        return

    for i in range(N):
        for j in range(N):
            if room[i][j] == "X":
                room[i][j] = "O"
                dfs(set_obstacle + 1)
                room[i][j] = "X"


def check_student(i, j):
    for direction in range(4):
        radius = 1
        while True:
            check_i = i + di[direction] * radius
            check_j = j + dj[direction] * radius
            if 0 <= check_i < N and 0 <= check_j < N:
                if room[check_i][check_j] == "X" or room[check_i][check_j] == "S":
                    radius += 1
                    continue
                elif room[check_i][check_j] == "O":
                    break
                else:
                    return False
            else:
                break

    return True


N = int(input())
room = [list(input().split()) for _ in range(N)]
student_points = []
set_obstacle = 0
result = "NO"

for i in range(N):
    for j in range(N):
        if room[i][j] == "S":
            student_points.append((i, j))

students = len(student_points)
dfs(set_obstacle)
print(result)