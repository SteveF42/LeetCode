class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # O(n) time compexity
        # O(1) space complexity
        
        l,r = 0,1

        profit = 0
        while r < len(prices):
            profit = max(profit,prices[r]-prices[l])

            if prices[l] < prices[r]:
                r+=1
            elif prices[l] >= prices[r]:
                l = r
                r += 1
        return profit
    
s = Solution()

print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([7,6,4,3,1]))
print(s.maxProfit([1,2]))
