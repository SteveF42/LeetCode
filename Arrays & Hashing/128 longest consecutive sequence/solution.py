class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        #O(n) space
        #O(n) time
        table = set(nums)

        longest = 0
        for i in nums:
            if i-1 not in table:
                sequence = 1
                while i+1 in table:
                    sequence += 1
                    i+=1
                longest = max(longest,sequence)
        
        return longest

s = Solution()

t = s.longestConsecutive([0,100,2,3,1,5,6,4])
print(t)