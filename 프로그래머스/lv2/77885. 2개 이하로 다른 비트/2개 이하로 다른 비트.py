def func(num):
    check = 1
    result = 0
    bin_num = bin(num)[2:][::-1] + '0'
    if bin_num[0] == '1':
        for i in range(len(bin_num)):
            if bin_num[i] == '0':
                num -= 2 ** (i - 1)
                num += 2 ** i
                return num
    else:
        return num + 1
    

def solution(numbers):
    answer = []
    for num in numbers:
        answer.append(func(num))
    return answer