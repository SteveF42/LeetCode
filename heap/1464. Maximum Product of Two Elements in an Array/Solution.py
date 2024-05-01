class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxVal = 0
        heapq.heapify(nums)
        print(nums)
        return (nums[-1] - 1) * (nums[-2]-1)