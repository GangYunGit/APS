from heapq import heappop, heappush

def solution(scoville, K):
    heap = []
    count = 0
    for food in scoville:       # 모든 음식을 heap에 push하면 자동으로 오름차순으로 정렬됨
        heappush(heap, food)
    while True:
        if heap[0] >= K:
            break
        first_food = heappop(heap)
        second_food = heappop(heap)
        mixed_food = first_food + second_food * 2
        count += 1
        if not heap and mixed_food < K:
            return -1
        heappush(heap, mixed_food)
    return count