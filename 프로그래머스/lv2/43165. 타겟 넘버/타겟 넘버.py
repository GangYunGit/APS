def solution(numbers, target):
    count = 0
    result = []
    def dfs(idx, sum_num):
        nonlocal count
        if idx == len(numbers):
            if sum_num == target:
                count += 1
            return
        
        else:
            dfs(idx + 1, sum_num + numbers[idx])
            dfs(idx + 1, sum_num - numbers[idx])
                
    dfs(0, 0)
    
    return count