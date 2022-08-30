# Runtime: 77 ms, faster than 5.27% of Python3 online submissions for Swap Nodes in Pairs.
# Memory Usage: 13.8 MB, less than 65.17% of Python3 online submissions for Swap Nodes in Pairs.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.swapper(head)
        
    def swapper(self,head):
        if(head is None):
            return None
        second = head
        new_head = head.next
        if(new_head is None):
            return head
        
        second.next = self.swapper(new_head.next)
        new_head.next = second
        return new_head