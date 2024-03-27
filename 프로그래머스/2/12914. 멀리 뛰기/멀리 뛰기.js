function solution(n) {
    var answer = 0;
    const dp = Array(2001).fill(0)
    dp[1] = 1
    dp[2] = 2
    for (let i = 3; i < 2001; i++) {
        dp[i] = (dp[i - 2] + dp[i - 1]) % 1234567
    }
    answer = dp[n]
    return answer;
}