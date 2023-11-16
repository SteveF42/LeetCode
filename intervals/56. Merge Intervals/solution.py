class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for start, end in intervals:
            prev_start, prev_end = res[-1]
            if prev_end >= start:
                res[-1][1] = max(prev_end,end)
            else:
                res.append([start,end])
        return res