# stackSize = 10
# stack = [0] * stackSize
# top = -1
#
# top += 1
# stack[top] = 1
# print(top, stack)
#
# top += 1
# stack[top] = 2
# print(top, stack)
#
# top -= 1
# temp = stack[top + 1]
# print(temp)
#
# temp = stack[top]
# top -= 1
# print(temp)
# print(top, stack)
#
# stack2 = []
# stack2.append(10)
# print(stack2)
# stack2.append(20)
# print(stack2)
# print(stack2.pop())
# print(stack2)
# print(stack2.pop())
# print(stack2)
# print(stack2)

# 크기가 N인 배열의 모든 원소에 접근하는 재귀함수

# def f(i, N):
#     if i == N:          # 모든 원소에 접근 완료
#         return
#     else:               # 남은 원소가 있는 경우
#         B[i] = A[i]
#         print(A[i])
#         f(i + 1, N)     # 다음 원소로 이동
# N = 3
# A = [1, 2, 3]
# B = [0] * N
# f(0, N)
# print(B)
#
#
# # ---------------
#
# def f(i, N):
#     if i == N:          # 모든 원소에 접근 완료
#         return
#     else:               # 남은 원소가 있는 경우
#         print(i)
#         f(i + 1, N)     # 다음 원소로 이동
# f(0, 1000)

# def f(n):
#     if memo[n] == -1:
#         memo[n] = f(n - 1) + f(n - 2)
#     return memo[n]
#
#
# memo = [-1] * 101
# memo[0] = 0
# memo[1] = 1
# for i in range(101):
#     print(i, f(i))
#     print(memo)


# def fibo_dp(n):
#     table[0] = 0
#     table[1] = 1
#     for i in range(2, n + 1):
#         table[i] = table[i - 1] + table[i - 2]
#     return
#
# table = [0] * 101
# fibo_dp(100)
# print(table[28])

# A~G -> 0~6
adjList = [[1, 2],      # 0
           [0, 3, 4],   # 1
           [0, 4],      # 2
           [1, 5],      # 3
           [1, 2, 5],   # 4
           [3, 4, 6],   # 5
           [5]]         # 6

def dfs(v, N):
    top = -1

    visited[v] = 1     # 시작점 방문
    print(v)
    while True:
        for w in adjList[v]:        # v의 인접 정점 중 방문 안 한 정점 w가 있으면
            if visited[w] == 0:
                top += 1            # push(v);
                stack[top] = v
                v = w               # v <- w; (w에 방문)
                visited[w] = 1          # visitied[w] <- true;
                print(v)            # 방문해서 하는 일(출력)
                break
        else:                       # w가 없으면
            if top != -1:            # 스택이 비어있지 않은 경우
                v = stack[top]          # pop
                top -= 1
            else:                   # 스택이 비어있으면
                break               # while을 빠져나옴

N = 7
visited = [0] * N   # visited 생성
stack= [0] * N      # stack 생성
dfs(1, N)
print()