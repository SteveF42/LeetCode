class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = max(nums)
        res = -1
        for i,num in enumerate(nums):
            if num == largest:
                res = i
                continue
            if num * 2 > largest:
                return -1
        
        return res