def solution(tickets):
    route = ['ICN']
    answer = []
    tickets.sort(reverse=True)
    print(tickets)
    visited = [False for _ in range(len(tickets))]
    
    def dfs(next_ticket):
        nonlocal answer
        if len(route) == len(tickets) + 1:
            answer = route[:]
            return

        for i in range(len(tickets)):
            if not visited[i] and tickets[i][0] == next_ticket:
                visited[i] = True
                route.append(tickets[i][1])
                dfs(tickets[i][1])
                route.pop()
                visited[i] = False
    
    dfs('ICN')
    
    return answer
