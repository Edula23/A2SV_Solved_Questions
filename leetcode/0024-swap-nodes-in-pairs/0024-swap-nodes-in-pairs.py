# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev = ListNode(-1)
        tail = prev
        def rec(i, j):
            nonlocal tail, prev
            
            if not i or not j or not i.next:
                
                if i and not j:
                    tail.next = ListNode(i.val)
                return prev.next
            
            node1 = ListNode(j.val)
            node2 = ListNode(i.val)
           
            tail.next = node1
            node1.next = node2
            tail = tail.next.next
            
            if i.next and j.next:
                return rec(i.next.next, j.next.next)
            else:
                return rec(None, None)
        return rec(head, head.next)