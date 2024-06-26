# space complexity: O(n)
# time complexity: O(n)

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and s in goal + goal