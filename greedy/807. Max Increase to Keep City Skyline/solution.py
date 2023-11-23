class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row = [0] * len(grid)
        cols = [0] * len(grid)

        # find maxes in both rows and cols
        for i in range(len(grid)):
            temp = 0
            for j in range(len(grid[i])):
                cols[j] = max(cols[j],grid[i][j])
                temp = max(temp,grid[i][j])
            row[i] = max(temp,row[i])


        res = 0
        for r in range(len(row)):
            for c in range(len(cols)):
                res += abs(min(row[r],cols[c]) - grid[r][c])
        
        return res