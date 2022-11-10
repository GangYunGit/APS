# BOJ_17114. 하이퍼 토마토

def bfs(dimension):
    pass


dimension = list(map(int, input().split()))
product = 1
for i in range(1, 11):
    product *= dimension[i]

house = [list(map(int, input().split())) for _ in range(product)]

print(dimension)
print(house)
visited = [[False] * dimension[0] for _ in range(product)]
# for i in range(1, 11):
#
print(visited)