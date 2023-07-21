'''
f(n) = f(n - 1) + f(n - 1) + 0이 5^(n - 1)개 + f(n - 1) + f(n - 1)
'''

def function(n, section):
    if n == 1:
        if section < 2:
            return section
        elif section > 2:
            return section - 1
        else:
            return 2
    
    q = section // (5 ** (n - 1))
    r = section % (5 ** (n - 1))
    
    if q < 2:
        return 4 ** (n - 1) * q + function(n - 1, r)
    elif q > 2:
        return 4 ** (n - 1) * (q - 1) + function(n - 1, r) 
    else:
        return 4 ** (n - 1) * 2
    
    
def solution(n, l, r):
    return function(n, r) - function(n, l - 1)

