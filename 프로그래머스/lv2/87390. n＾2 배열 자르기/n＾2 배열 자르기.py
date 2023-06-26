def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        # i // n => 행의 좌표, i % n => 열의 좌표
        # 문제에서 주어진 2차원 배열의 각 칸의 값은 열과 행의 좌표 중 "크거나 같은 수 + 1"을 따라감
        answer.append(max(i // n, i % n) + 1)
    return answer