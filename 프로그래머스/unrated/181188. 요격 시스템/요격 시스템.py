def solution(targets):
    targets.sort(key=lambda x: x[1])
    answer = 1
    compare = targets[0]
    
    for i in range(len(targets) - 1):
        if compare[1] <= targets[i + 1][0]:
            answer += 1
            compare = targets[i + 1]
        
    return answer