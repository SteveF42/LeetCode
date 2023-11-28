# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.paths = 0

        def search(root,val):
            if root == None:
                return
            if root.val == val:
                self.paths += 1
            search(root.left, val - root.val)
            search(root.right, val - root.val)
            
        def dfs(root):
            if root == None:
                return

            search(root,targetSum)

            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.paths