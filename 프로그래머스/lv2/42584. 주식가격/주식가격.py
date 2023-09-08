def solution(prices):
    answer = [0] * len(prices)
    stack = []
    now_second = 0
    for price in prices:
        while True:
            if not stack or stack[-1][0] <= price:
                break
            stock_price, stock_second = stack.pop()
            answer[stock_second] = now_second - stock_second
        stack.append((price, now_second))
        now_second += 1
    
    for price, second in stack:
        answer[second] = now_second - 1 - second
    
    return answer