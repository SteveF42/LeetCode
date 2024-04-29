# O(n^2) time complexity
# O(1) space complexity

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0

        for i in range(len(arr)):
            t = 0
            for j in range(i,len(arr)):
                size = j - i + 1
                t += arr[j]
                if size % 2 == 1:
                    res += t

        return res   
            