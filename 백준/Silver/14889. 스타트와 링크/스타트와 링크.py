import sys
input = sys.stdin.readline


def dfs(start, end):
    global min_state_gap

    if len(start_team) == N // 2:
        start_team_state = 0
        link_team_state = 0
        link_team = list(set(all_team) - set(start_team))

        for i in range(N // 2):
            for j in range(i, N // 2):
                start_team_state += state_list[start_team[i]][start_team[j]] + state_list[start_team[j]][start_team[i]]
                link_team_state += state_list[link_team[i]][link_team[j]] + state_list[link_team[j]][link_team[i]]
        min_state_gap = min(min_state_gap, abs(start_team_state - link_team_state))
        return

    for i in range(start, end):
        start_team.append(i)
        dfs(i + 1, end)
        start_team.pop()


N = int(input())
state_list = [list(map(int, input().split())) for _ in range(N)]
team_state = []

start_team = []
all_team = [_ for _ in range(N)]
min_state_gap = 100 * N * N
dfs(0, N)
print(min_state_gap)
