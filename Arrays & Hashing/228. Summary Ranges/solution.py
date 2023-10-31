class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # O(n) time
        # O(1) space
        
        res = []
        l = 0

        while l < len(nums):
            r = l
            while r < len(nums)-1:
                if nums[r] + 1 == nums[r+1]:
                    r += 1
                else:
                    break
            if l == r:
                res.append(f'{nums[l]}')
            else:
                res.append(f'{nums[l]}->{nums[r]}')
            l = r + 1
        return res