N, M = map(int, input().split())
hear = set()
look = set()
result = []

for _ in range(N):
    input_name = input()
    hear.add(input_name)

for _ in range(M):
    input_name = input()
    look.add(input_name)

result = sorted(list(hear & look))
print(len(result))
print(*result, sep='\n')