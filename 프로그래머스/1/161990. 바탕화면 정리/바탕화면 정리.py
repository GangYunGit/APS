def solution(wallpaper):
    
    row_size = len(wallpaper)
    col_size = len(wallpaper[0])
    lux, luy = row_size, col_size
    rdx, rdy = 0, 0
    for i in range(row_size):
        for j in range(col_size):
            if wallpaper[i][j] == '#':
                lux = min(lux, i)
                luy = min(luy, j)
                rdy = max(rdy, j)
                rdx = max(rdx, i)
    answer = [lux, luy, rdx + 1, rdy + 1]
    return answer