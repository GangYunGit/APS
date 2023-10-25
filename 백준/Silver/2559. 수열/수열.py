n, k = map(int, input().split())
temp = list(map(int, input().split()))
start_idx, end_idx = 0, k - 1
temp_sum = sum(temp[start_idx: end_idx + 1])
max_sum = temp_sum
while end_idx < n - 1:
    temp_sum -= temp[start_idx]
    start_idx += 1
    end_idx += 1
    temp_sum += temp[end_idx]
    max_sum = max(temp_sum, max_sum)
print(max_sum)