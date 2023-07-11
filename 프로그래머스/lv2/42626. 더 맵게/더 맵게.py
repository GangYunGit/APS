from heapq import heappop, heappush

def solution(scoville, K):
    heap = []
    count = 0
    for food in scoville:
        heappush(heap, food)
    while True:
        first_food = heappop(heap)
        if first_food >= K:
            break
        second_food = heappop(heap)
        mixed_food = first_food + second_food * 2
        count += 1
        if not heap and mixed_food < K:
            return -1
        heappush(heap, mixed_food)
    return count