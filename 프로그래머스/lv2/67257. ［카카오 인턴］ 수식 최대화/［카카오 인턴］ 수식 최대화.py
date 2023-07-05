from itertools import permutations
from copy import deepcopy

def operate(operators, operate_list):
    for operator in operators:
        stack = []
        while True:
            if not operate_list:
                break
            temp = operate_list.pop(0)
            if temp == operator:
                num1 = stack.pop()
                num2 = operate_list.pop(0)
                stack.append(calculate(num1, num2, operator))
            else:
                stack.append(temp)
        operate_list = stack
    
    return abs(stack.pop())


def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    

def solution(expression):
    answer = 0
    operate_list = []
    
    number = ""
    for item in expression:
        if item.isdecimal():
            number += item
        else:
            operate_list.append(int(number))
            operate_list.append(item)
            number = ""
    operate_list.append(int(number))
    
    operate_order = permutations(['*', '+', '-'], 3)
    for operators in operate_order:
        answer = max(operate(operators, deepcopy(operate_list)), answer)
        
    return answer