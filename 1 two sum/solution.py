class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #O(n) space
        #O(n) time
        
        lookUp = {}
        for i,num in enumerate(nums): 
            ans = lookUp.get(num)
            if ans != None:
                return (ans,i)
            lookUp[target-num] = i