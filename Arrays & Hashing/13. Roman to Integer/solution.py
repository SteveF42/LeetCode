class Solution:
    def romanToInt(self, s: str) -> int:
        # O(n) runtime
        # O(1) space
        r = len(s)-1
        m = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        res = 0
        while r > 0:
            print(r)
            c1 = s[r]
            c2 = s[r-1]
            if m[c1] > m[c2]:
                res += abs(m[c1]-m[c2])
                r -= 2
            else:
                res += m[c1]
                r -= 1
        
        if r == 0:
            res += m[s[0]]
        return res
