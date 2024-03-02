# O(n) time | O(1) space

class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        res = 0
        for l in range(len(nums)):
            if nums[l] % 2 == 1 or nums[l] > threshold:
                continue
            r = l
            
            while r < len(nums)-1:
                if nums[r] > threshold or nums[r+1] > threshold or nums[r] % 2 == nums[r+1] % 2:
                    break
                r += 1
            res = max(res,(r-l) + 1)
            l = r+1
        return res