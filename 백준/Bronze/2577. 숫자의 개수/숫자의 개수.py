num = int(input()) * int(input()) * int(input())
num = str(num)
count = [0] * 10
for i in num:
    count[int(i)] += 1
print(*count, sep="\n")