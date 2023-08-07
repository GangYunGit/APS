# def solution(w,h):
#     i = 1
#     a = 0
#     break_point = min(w, h)
#     while i <= break_point:
#         if not w % i and not h % i:
#             a = i
#         i += 1
        
#     answer = w * h - (w + h - a)
#     return answer

import math

def solution(w,h):
        
    answer = w * h - (w + h - math.gcd(w, h))
    return answer