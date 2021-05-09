class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m) :
            for j in range(n) :
                next_value = dp[i][j] + 1 if word1[i] == word2[j] else dp[i][j]
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j], next_value)
        return m + n - 2 * dp[m][n]

