from collections import deque

def solution(n, computers):
    def bfs(v):
        visited[v] = True
        queue = deque()
        queue.append(v)
        
        while queue:
            v = queue.popleft()
            for next_v in range(n):
                if not visited[next_v] and computers[v][next_v] == 1:
                    visited[next_v] = True
                    queue.append(next_v)
    
    visited = [False] * n
    answer = 0
    for v in range(n):
        if not visited[v]:
            bfs(v)
            answer += 1
            
    return answer