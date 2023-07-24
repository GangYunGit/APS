def solution(storey):
    answer = 0
    while True:

        r = storey % 10         # 입력 받은 수의 오른쪽 끝 자릿수를 가져옴
            
        if r < 5:               # 가져온 숫자가 5보다 작으면
            answer += r         # 그냥 더함
        elif r > 5:             # 5보다 크면
            answer += 10 - r    # 10에서 해당 숫자를 뺀 수를 더해주고
            storey += 10        # 다음 자릿수를 하나 중가시킴
        else:                               # 가져온 숫자가 5일 때
            if (storey // 10) % 10 >= 5:    # 바로 다음 자릿수가 5보다 크거나 같으면
                storey += 10                # 다음 자릿수를 하나 중가시키고
            answer += r                     # 결과에 더해줌
        
        if storey == 0:         # 숫자를 다 확인하면 탈출
            break         
        
        storey //= 10
        
    return answer