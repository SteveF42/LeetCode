class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        m = {}
        res = 0
        for row in grid:
            m[tuple(row)] = m.get(tuple(row),0) + 1
        for i in range(len(grid)):
            cols = []
            for j in range(len(grid[i])):
                cols.append(grid[j][i])
            if tuple(cols) in m:
                res += m[tuple(cols)]
        return res