class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        s = set() # O(n) space

        for i in nums: # O(n) time
            if i in s:
                return True
            s.add(i)
        
        return False



testCases = [
    ([1,2,3,1],True),
    ([1,2,3,4],False),
    ([1,1,1,3,3,4,3,2,4,2],True)
]


s = Solution()

for test in testCases:
    assert s.containsDuplicate(test[0]) == test[1], f"{test[0]} Should return {test[1]}" 

print("all casses pass")

# Answer accepted 