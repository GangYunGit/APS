koong = [1, 1, 2, 4] + [0] * 65
for i in range(4, 68):
    koong[i] = koong[i - 1] + koong[i - 2] + koong[i - 3] + koong[i - 4]
t = int(input())
for _ in range(t):
    print(koong[int(input())])