from itertools import permutations

nums = []
nums_set = set()

n = int(input())
k = int(input())

for _ in range(n):
    nums.append(input())
    
for comb in permutations(nums, k):
    get_num = "".join(comb)
    nums_set.add(get_num)
    
print(len(nums_set))