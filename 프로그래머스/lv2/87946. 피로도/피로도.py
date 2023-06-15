def solution(k, dungeons):
    answer = -1
    choice = []
    visited = [False for _ in range(len(dungeons))]
    max_count = 0
    def dfs(end):
        nonlocal choice, max_count
        if len(choice) == end:
            fatigue = k
            count = 0
            for i in range(len(choice)):
                if fatigue >= choice[i][0]:
                    count += 1
                    fatigue -= choice[i][1]
                else:
                    break
                    
            max_count = max(count, max_count)
            
            return 
        
        for i in range(end):
            if not visited[i]:
                visited[i] = True
                choice.append(dungeons[i])
                dfs(end)
                visited[i] = False
                choice.pop()
    
    dfs(len(dungeons))
        
    return max_count