def solution(triangle):
    memo = triangle
    bottom = len(triangle)
    for i in range(1, bottom):
        for j in range(i + 1):
            if i == 1:
                memo[i][j] += memo[i - 1][0]
            else:
                if j == 0:
                    memo[i][j] += memo[i - 1][j]
                elif j == i:
                    memo[i][j] += memo[i - 1][i - 1]
                else:
                    memo[i][j] += max(memo[i - 1][j - 1], memo[i - 1][j])
    # print(memo)
    return max(memo[bottom - 1])