# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # O(n) time
        # O(1) space
        
        slow = fast = head

        while fast:
            slow = slow.next
            fast = fast.next.next
        
        prev = None

        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        res = 0
        ls1 = head
        ls2 = prev
        while ls2:
            res = max(res,ls2.val + ls1.val)
            ls1 = ls1.next
            ls2 = ls2.next
        
        return res