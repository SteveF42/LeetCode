class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # O(log(n) * log(m)) time
        # O(1) space
        
        ROW,COL = len(matrix)-1,len(matrix[0])-1

        top,bot = 0, ROW

        while top <= bot:
            mid = (bot+top)//2
            if matrix[mid][-1] < target:
                top = mid + 1
            elif matrix[mid][0] > target:
                bot = mid -1
            else:
                break
            
        if not (top <= bot):
            return False
        
        l,r = 0,COL
        row = (top + bot)//2
        while l <= r:
            mid = (l+r)//2
            if matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        col = (l+r)//2
        return matrix[row][col] == target