function solution(n) {
    var answer = 0;
    const fibo = [0, 1];
    for (let i = 0; i < n + 1; i ++) {
        if (i > 1) {
            fibo.push((fibo[i - 1] + fibo[i - 2]) % 1234567)
        }
    }
    answer = fibo[n] 
    return answer;
}