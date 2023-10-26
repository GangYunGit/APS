n = int(input())
balloon = list(map(int, input().split()))
dart = [0] * 1000001

for i in balloon:
    if dart[i] == 0:
        dart[i] += 1
    dart[i] -= 1
    dart[i - 1] += 1

print(sum(dart))