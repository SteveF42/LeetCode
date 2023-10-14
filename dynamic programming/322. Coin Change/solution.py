class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # O(n * c) time where n is the amount and c the number of coins
        # O(n) space for each amount
        
        dp = [amount+1 for x in range(amount+1)]
        dp[0] = 0

        for i in range(1,amount+1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i],1 + dp[i-c])
        

        return dp[amount] if dp[amount] != amount + 1 else -1

        dp = {}
        def dfs(a):
            if a in dp:
                return dp[a]
            if a == 0:
                return 0
            
            dp[a] = amount + 1
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a],1+dfs(a-c))
            return dp[a]

        res = dfs(amount)
        return res if res != amount + 1 else -1