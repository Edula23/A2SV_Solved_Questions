# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        count = n = 0
        while curr:
            count += 1
            curr = curr.next
        curr = head
        if count % 2 == 0:
            n = count//2
            for i in range(n):
                curr = curr.next
        else:
            n = ceil(count/2)
            for i in range(n-1):
                curr = curr.next       

        return curr


        
        