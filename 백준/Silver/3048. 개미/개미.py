ant1_num, ant2_num = map(int, input().split())
ant1 = list(input())[::-1]
ant2 = list(input())
second = int(input())

ant_line = ['' for _ in range(ant2_num * 2)]

for i in range(ant2_num):
    ant_line[i * 2] = ant2[i]

new_ant_line = ['' for _ in range(ant1_num * 2)] + ant_line + ['' for _ in range(100)]

for i in range(ant1_num):
    new_ant_line[(i + second) * 2 + 1] = ant1[i]


for ant in new_ant_line:
    if ant != '':
        print(ant, end='')
