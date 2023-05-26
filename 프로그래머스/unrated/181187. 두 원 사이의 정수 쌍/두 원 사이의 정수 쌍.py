import math

def solution(r1, r2):
    answer = 0
    for i in range(1, r2 + 1):
        h2 = math.floor(abs(r2 ** 2 - i ** 2) ** 0.5)
        h1 = 0
        if r1 > i:
            h1 = math.ceil(abs(r1 ** 2 - i ** 2) ** 0.5)
        answer += h2 - h1 + 1

    return answer * 4