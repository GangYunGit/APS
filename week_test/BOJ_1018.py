# 1018_체스판_다시_칠하기

M, N = map(int, input().split())

my_board = [input() for _ in range(M)]
white_chess_board = ['' for _ in range(8)]
black_chess_board = ['' for _ in range(8)]

print(my_board)

for i in range(8):
    if i % 2:
        white_chess_board[i] = 'BWBWBWBW'
    else:
        white_chess_board[i] = 'WBWBWBWB'

for i in range(8):
    if i % 2:
        black_chess_board[i] = 'WBWBWBWB'
    else:
        black_chess_board[i] = 'BWBWBWBW'

print(white_chess_board)