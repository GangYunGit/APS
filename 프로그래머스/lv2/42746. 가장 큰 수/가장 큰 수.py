def solution(numbers):
    answer = ""
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])
    numbers.sort(key=lambda x: x * 3, reverse=True)
    for num in numbers:
        answer += num
    return str(int(answer))