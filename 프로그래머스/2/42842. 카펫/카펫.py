def solution(brown, yellow):
    answer = []
    width, height = 0, 0
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            w = yellow // i
            h = i
            if (2 * (w + 2) + 2 * (h + 2) - 4) == brown:
                answer = [w + 2, h + 2]
                break
    return answer