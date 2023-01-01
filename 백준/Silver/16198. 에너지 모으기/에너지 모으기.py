def dfs(marbles, sum_energy):
    global max_energy
    remain_marbles = len(marbles)
    if remain_marbles == 2:
        max_energy = max(sum_energy, max_energy)
        return

    for i in range(1, remain_marbles - 1):
        energy = marbles[i - 1] * marbles[i + 1]
        sum_energy += energy
        pop_marble = marbles.pop(i)
        dfs(marbles, sum_energy)
        sum_energy -= energy
        marbles.insert(i, pop_marble)


N = int(input())
max_energy = 0
marbles = list(map(int, input().split()))
dfs(marbles, 0)
print(max_energy)