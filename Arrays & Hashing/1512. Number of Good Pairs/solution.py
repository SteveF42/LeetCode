class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        friends = {}

        res = 0
        for i in nums:
            friendCount = friends.get(i,0)
            res += friendCount
            friends[i] = friendCount + 1

        return res