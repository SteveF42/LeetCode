# O(n) solution
# O(1) space

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        l,r = 0,k
        s = str(num)

        res = 0
        while r <= len(s):
            curr = int(s[l:r])
            if curr > 0 and num % curr == 0:
                res += 1

            l += 1
            r += 1

        return res