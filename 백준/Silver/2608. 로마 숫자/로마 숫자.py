def rome_to_arabia(rome_num):
    arabia_num = 0
    i = 0
    while True:
        if i == len(rome_num):
            break
        if i < len(rome_num) - 1 and rome_num[i] + rome_num[i + 1] in rome_rule.keys():
            arabia_num += rome_rule[rome_num[i] + rome_num[i + 1]]
            i += 2
        else:
            arabia_num += rome_rule[rome_num[i]]
            i += 1

    return arabia_num


def arabia_to_rome(arabia_num):
    rome_num = ''
    for rome_checker in rome_rule.keys():
        while arabia_num >= rome_rule[rome_checker]:
            rome_num += rome_checker
            arabia_num -= rome_rule[rome_checker]
    return rome_num


rome_rule = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC':90, 'L': 50, 'XL': 40, 'X': 10, 'IX':9, 'V': 5, 'IV': 4, 'I': 1}
r_num1, r_num2 = input(), input()
sum_num = rome_to_arabia(r_num1) + rome_to_arabia(r_num2)
print(sum_num)
print(arabia_to_rome(sum_num))