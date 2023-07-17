def slope_checker(road_info):
    slope_installed = [False for _ in range(n)]
    idx = 0
    former_height = road_info[idx]
    while idx <= n - 1:
        if former_height - road_info[idx] == 1:

            for i in range(idx, idx + l):
                if 0 <= i < n - 1:
                    slope_installed[i] = True

            length_checker = 1
            for i in range(idx, idx + l - 1):
                if 0 <= i < n - 1:
                    if road_info[i] == road_info[i + 1]:
                        length_checker += 1
            if length_checker != l:
                return False

            former_height = road_info[idx]
            idx += 1
            continue

        elif former_height - road_info[idx] == -1:
            length_checker = 1
            for i in range(idx - l, idx):
                if slope_installed[i]:
                    return False

                if 0 <= i < n - 1:
                    if road_info[i] == road_info[i + 1]:
                        length_checker += 1
            if length_checker != l:
                return False
            former_height = road_info[idx]
            idx += 1
            continue

        elif former_height - road_info[idx] == 0:
            idx += 1
            continue
        else:
            return False

    return True


n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
count = 0

for i in range(n):
    if slope_checker(board[i]):
        count += 1

    if slope_checker(list(zip(*board))[i]):
        count += 1

print(count)