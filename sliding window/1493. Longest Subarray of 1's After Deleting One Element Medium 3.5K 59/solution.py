class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # O(n) time
        # O(1) space
        zeros = 0
        l = 0
        res = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1
            
            while zeros > 1:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            res = max(res,(r-l))            

        return res