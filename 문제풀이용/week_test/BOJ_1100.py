# 1100_하얀칸

board = [input() for _ in range(8)]
count = 0

for i in range(8):
    for j in range(8):
        if i % 2:
            if j % 2 == 1 and board[i][j] == 'F':
                count += 1
        else:
            if j % 2 == 0 and board[i][j] == 'F':
                count += 1

print(count)


