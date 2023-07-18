def solution(storey):
    answer = 0
    while True:

        r = storey % 10
            
        if r < 5:
            answer += r
        elif r > 5:
            answer += 10 - r
            storey += 10
        else:
            if (storey // 10) % 10 >= 5:
                storey += 10
            answer += r        
        
        if storey == 0:
            break         
        
        storey //= 10
        
    return answer