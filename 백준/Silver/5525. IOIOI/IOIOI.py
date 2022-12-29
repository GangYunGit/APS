N = int(input())
M = int(input())
S = input()

compare = 'IO' * N + 'I'
IOI_count = 0
count = 0
for i in range(M):
    if i == 0 and S[i] == 'I':
        IOI_count += 1
    if i > 0:
        if IOI_count > 0 and S[i] != S[i - 1]:
            IOI_count += 1
        else:
            if S[i] == 'O':
                IOI_count = 0
            else:
                IOI_count = 1

    if IOI_count % 2 and IOI_count >= 2 * N + 1:
        count += 1

print(count)