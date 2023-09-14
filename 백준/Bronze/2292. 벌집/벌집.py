room = [1] + [0] * 18257
n = int(input())
for i in range(1, 18258):
    room[i] = room[i - 1] + 6 * i
for i in range(18258):
    if n <= room[i]:
        print(i + 1)
        break