# p3_DFS

import sys

sys.stdin = open('input.txt')


adjList = [[1, 2],      # 0
           [0, 3, 4],   # 1
           [0, 6],      # 2
           [1, 5],      # 3
           [1, 5],      # 4
           [3, 4, 6],   # 5
           [2,5]]       # 6


def dfs(v, N):
    top = -1

    visited[v] = 1     # 시작점 방문
    print(v + 1)
    while True:
        for w in adjList[v]:        # v의 인접 정점 중 방문 안 한 정점 w가 있으면
            if visited[w] == 0:
                top += 1            # push(v);
                stack[top] = v
                v = w               # v <- w; (w에 방문)
                visited[w] = 1          # visitied[w] <- true;
                print(v + 1)            # 방문해서 하는 일(출력)
                break
        else:                       # w가 없으면
            if top != -1:            # 스택이 비어있지 않은 경우
                v = stack[top]          # pop
                top -= 1
            else:                   # 스택이 비어있으면
                break               # while을 빠져나옴

visited = [0] * 7   # visited 생성
stack = [0] * 7     # stack 생성
dfs(0, 7)


