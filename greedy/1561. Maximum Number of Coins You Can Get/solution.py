class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        res = 0
        l, r = 0,len(piles)-1

        piles.sort()

        while l < r:
            res += piles[r-1]
            l += 1
            r -= 2
        
        return res