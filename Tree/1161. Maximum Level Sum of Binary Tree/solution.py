# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)

        depth = defaultdict(int)
        i = 1
        while q:
            size = len(q)
            for _ in range(size):
                curr = q.popleft()
                if curr:
                    depth[i] += curr.val
                    q.append(curr.left)
                    q.append(curr.right)
            i += 1
        
        return max(depth,key=depth.get)