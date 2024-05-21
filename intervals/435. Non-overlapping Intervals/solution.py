# O(nlogn) time complexity
# O(1) space complexity

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        res = 0
        prevEnd = intervals[0][1]
        for start,end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = max(end, prevEnd)
        
        return res