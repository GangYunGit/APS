formula = input()
nums = list(map(int, formula.replace('-', ' ').replace('+', ' ').split()))
calculators = []

for i in formula:
    if not i.isdecimal():
        calculators.append(i)

cut_idx = [0]
for i in range(len(calculators)):
    if calculators[i] == '-':
        cut_idx.append(i + 1)
cut_idx.append(len(nums))

result = sum(nums[:cut_idx[1]])
for i in range(1, len(cut_idx) - 1):
    result -= sum(nums[cut_idx[i]:cut_idx[i + 1]])
print(result)