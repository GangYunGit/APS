def solution(tickets):
    route = ['ICN']                 # 항상 ICN공항에서 시작
    answer = []         
    # 내림차순으로 정렬해놓으면 경로가 여러개 일 때 알파벳 순서가 가장 앞서는 공항이 마지막에 탐색됨
    tickets.sort(key=lambda x: x[1], reverse=True)
    visited = [False for _ in range(len(tickets))]
    
    ######## dfs 함수 시작 부분
    def dfs(next_ticket):
        nonlocal answer
        if len(route) == len(tickets) + 1:      # 모든 경로 탐색이 완료되었다면
            # print(route)
            answer = route[:]                   # answer에 경로를 저장
            return

        for i in range(len(tickets)):
            if not visited[i] and tickets[i][0] == next_ticket:     # 방문하지 않았고, 다음 공항을 발견했다면
                visited[i] = True                                   # 방문처리
                route.append(tickets[i][1])                         # 방문한 공항을 경로에 추가
                dfs(tickets[i][1])                                  # 다음 dfs 수행              
                route.pop()             # return문을 만난 이후: 이미 확인한 정점을 pop
                visited[i] = False      # 방문 처리도 해제
    ########## dfs 끝
    
    dfs('ICN')
    
    return answer
