int(input())
a = list(map(int, input().split()))
score, result = 0, 0
for i in a:
    if i == 1:
        score += 1
    else:
        score = 0
    result += score
print(result)