class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0

        res = 0
        ones = 0
        for r in range(len(nums)):
            if nums[r] == 1:
                ones += 1
            while ((r-l+1) - ones) > k:
                if nums[l] == 1:
                    ones -= 1
                l += 1
            res = max((r-l)+1,res)
            
        return res