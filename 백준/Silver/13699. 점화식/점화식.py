n = int(input())
t = [1] * (n + 1)
for i in range(2, n + 1):
    t_i = 0
    for j in range(i):
        t_i += t[i - j - 1] * t[j]
    t[i] = t_i
print(t[n])