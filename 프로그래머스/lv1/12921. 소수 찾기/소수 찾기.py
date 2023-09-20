def solution(n):
    answer = 0
    def prime_list(n):
        sieve = [True] * n
        m = int(n ** 0.5)
        for i in range(2, m + 1):
            if sieve[i]:
                for j in range(2 * i, n, i):
                    sieve[j] = False

        return sum(sieve[2:])
    
    answer = prime_list(n + 1)
    
    return answer