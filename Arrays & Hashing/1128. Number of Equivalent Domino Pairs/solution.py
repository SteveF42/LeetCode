# O(n) time | O(n) space

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        m = {}
        for dom in dominoes:
            l = tuple(sorted(dom))
            m[l] = m.get(l,0) + 1
        
        res = 0
        for val in m.values():
            s = val*(val-1)//2
            res += s
        return res
        