# first solution
# O(n) time | O(n) space

#second solution
# O(n) time | O(n) space

class Solution:
    def rob(self, nums: List[int]) -> int:
        # if len(nums) <= 1:
        #     return nums[0]
        # if len(nums) == 0:
        #     return 0
        
        # mem = [nums[0],max(nums[0],nums[1])]
        
        # for i in range(2,len(nums)):
        #     mem.append(max(mem[i-1],mem[i-2] + nums[i]))
            
        # return mem[-1]

        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i]
            if i >= len(nums):
                return 0
            if i == len(nums) - 1 or i == len(nums) - 2:
                return nums[i]
            
            dp[i] = nums[i]
            for j in range(i+2,len(nums)):
                dp[i] = max(dp[i],nums[i] + dfs(j))
            return dp[i]
        
        res = 0
        for i in range(len(nums)):
            res = max(res, dfs(i))
        
        return res
