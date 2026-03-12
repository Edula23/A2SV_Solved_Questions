# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head
        while curr:
            while stack and curr.val > stack[-1]:
                stack.pop()
            stack.append(curr.val) 
            curr = curr.next
        curr = head
        for i in range(len(stack)):
            curr.val = stack[i]
            if i == len(stack) - 1:
                curr.next = None
            else:
                curr = curr.next            
        return head