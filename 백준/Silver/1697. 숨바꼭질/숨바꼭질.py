from collections import deque


def bfs(v):
    queue = deque()
    min_depth = 100000000
    if v == K:
        return 0
    
    visited[v] = True
    for first_method in range(1, 4):
        depth = 1
        queue.append((move[first_method](v), depth))

    while queue:
        temp_n, depth = queue.popleft()
        visited[temp_n] = True
        # print(temp_n)
        if temp_n == K:
            if depth < min_depth:
                min_depth = depth
            break
        depth += 1

        for method in range(1, 4):
            next_n = move[method](temp_n)

            if 0 <= next_n < 100001 and not visited[next_n]:
                queue.append((next_n, depth))

    return min_depth


move = {
    1: lambda x: x - 1,
    2: lambda x: x + 1,
    3: lambda x: 2 * x
}

N, K = map(int, input().split())
visited = [False] * 200001
print(bfs(N))