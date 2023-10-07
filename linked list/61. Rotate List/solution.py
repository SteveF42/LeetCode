# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # O(n) time
        # O(1) space
        
        if not head:
            return None
        
        size = 1
        last = head
        while last.next:
            last = last.next
            size += 1
        k = k % size

        last.next = head

        temp = head
        for i in range(size - k - 1):
            temp = temp.next
        answer = temp.next
        temp.next = None
        return answer