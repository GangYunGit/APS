from collections import deque

def solution(land):
    
    row = len(land)
    col = len(land[0])
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    
    def bfs(i, j):
        queue = deque()
        queue.append((i, j))
        visited[i][j] = True
        route = []
        route.append((i, j))
        count = 1
        
        while queue:
            i, j = queue.popleft()
            for direction in range(4):
                ni, nj = i + di[direction], j + dj[direction]
                if not (0 <= ni < row and 0 <= nj < col):
                    continue
                if not visited[ni][nj] and land[ni][nj] == 1:
                    visited[ni][nj] = True
                    route.append((ni, nj))
                    count += 1
                    queue.append((ni, nj))
        
        for ri, rj in route:
            oil_amount[ri][rj] = (count, idx)
        
        return
    
    max_oil = 0
    oil_amount = [[(0, -1) for _ in range(col)]for _ in range(row)]
    visited = [[False] * col for _ in range(row)]
    idx = 0
    for i in range(row):
        for j in range(col):
            if not visited[i][j] and land[i][j] == 1:
                idx += 1
                bfs(i, j)
    
    for j in range(col):
        prev_oil = 0
        total_oil = 0
        group = set()
        for i in range(row):
            if prev_oil == 0 and oil_amount[i][j][1] not in group:
                total_oil += oil_amount[i][j][0]
                group.add(oil_amount[i][j][1])
                # print(oil_amount[i][j][0])
            prev_oil = oil_amount[i][j][0]
            # print()
        max_oil = max(total_oil, max_oil)
    answer = max_oil
    return answer