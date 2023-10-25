class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort(reverse=True)

        @lru_cache(maxsize=None)
        def dfs(i,total):
            if total == 0:
                return 1
            if total < 0 or i == len(coins):
                return 0
            
            res = dfs(i,total-coins[i])
            res += dfs(i+1,total)
            return res
        res = dfs(0,amount)
        return res