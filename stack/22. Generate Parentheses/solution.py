class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # O(N + n^2^n) time complexity
        # O(n) space
        res = []
        stack = []

        def backTrack(countOpen,countClosed):
            if countOpen == countClosed == n:
                res.append("".join(stack))
                return
            
            if countOpen < n:
                stack.append('(')
                backTrack(countOpen+1,countClosed)
                stack.pop()
            if countClosed < countOpen:
                stack.append(')')
                backTrack(countOpen,countClosed+1)
                stack.pop()
        
        backTrack(0,0)
        return res
    
s = Solution()
print(s.generateParenthesis(3))