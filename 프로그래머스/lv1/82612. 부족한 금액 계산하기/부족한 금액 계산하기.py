def solution(price, money, count):
    fee = money - count * (count + 1) // 2 * price
    if fee < 0 : 
        answer = -fee
    else:
        answer = 0
    return answer