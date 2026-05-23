# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n = ""
        def rec(curr):
            nonlocal n
            if not curr.next:
                n = str(curr.val)
                return n
            rec(curr.next)
            n = n + str(curr.val)

            return n
        n1 = int(rec(l1))
        n = ""
        n2 = int(rec(l2))
        res = str(n1 + n2)
         
        prev = ListNode(-1)
        tail = prev
        for i in range(len(res)):
            node = ListNode(int(res[-(i+1)]))
            tail.next = node
            tail = tail.next
        return prev.next


