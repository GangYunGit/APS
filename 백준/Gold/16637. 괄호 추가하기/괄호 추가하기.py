from itertools import combinations


def get_group_index(nums):
    max_size = (len(nums) // 2) * 2
    max_result = calculate(nums, calculator)
    # 묶음의 크기 지정(2개, 4개, 6개, ...)
    for size in range(2, max_size + 1, 2):

        # 묶어서 계산할 숫자의 인덱스 뽑기
        groups = []
        for comb in combinations(range(len(nums)), size):
            for i in range(0, size, 2):
                if comb[i + 1] - comb[i] != 1:
                    break
            else:
                groups.append(comb)
        # print(groups)

        for group in groups:
            new_nums = []
            calculator_idx = [_ for _ in range(len(calculator))]
            for i in range(len(nums)):
                new_num = nums[i]
                if i in group:
                    if i in [group[_] for _ in range(0, len(group), 2)]:
                        if calculator[i] == '+':
                            new_num += nums[i + 1]
                        elif calculator[i] == '-':
                            new_num -= nums[i + 1]
                        elif calculator[i] == '*':
                            new_num *= nums[i + 1]
                        new_nums.append(new_num)
                        calculator_idx.remove(i)
                else:
                    new_nums.append(new_num)
            new_calculator = [calculator[_] for _ in calculator_idx]
            # print(new_nums, new_calculator)
            max_result = max(max_result, calculate(new_nums, new_calculator))
    return max_result


def calculate(nums, calculator):
    result = nums[0]
    for i in range(len(calculator)):
        if calculator[i] == '+':
            result += nums[i + 1]
        elif calculator[i] == '-':
            result -= nums[i + 1]
        elif calculator[i] == '*':
            result *= nums[i + 1]
    return result


n = int(input())
formula = input()
nums = []
calculator = []
for i in formula:
    if i.isdecimal():
        nums.append(int(i))
    else:
        calculator.append(i)

print(get_group_index(nums))