class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # O(n) time
        # O(n) space for dp map
        
        stack = []
        stack.append(root)
        ans = 0
        dp = {}
        def maxZag(node,left):
            if node == None:
                return 0
            if node in dp:
                return dp[node]
            res = 1
            if left:
                res += maxZag(node.right,False)
            else:
                res += maxZag(node.left,True)
            dp[node] = res
            return dp[node]
        
        while stack:
            curr = stack.pop()
            if curr:
                l = maxZag(curr.left,True)
                r = maxZag(curr.right,False)
                ans = max(ans,max(l,r))
                stack.append(curr.left)
                stack.append(curr.right)
        return ans