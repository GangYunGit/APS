p = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0] * 90

for i in range(10, 100):
    p[i] = p[i - 1] + p[i - 5]

for _ in range(int(input())):
    print(p[int(input()) - 1])