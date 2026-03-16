class Node(object):
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyCircularDeque(object):

    def __init__(self, k: int):
        self.head = None
        self.size = 0
        self.k = k
        

    def insertFront(self, value: int) -> bool:
       
        node = Node(value) 
        # print(node.val)
        if self.size == 0:
            self.head = node
            node.next = node
            node.prev = node
            self.size += 1
            return True
        elif self.size >= self.k:
            return False
        else:
            # print(self.head.val)
            curr = self.head
            node.next = curr
            node.prev = curr.prev
            curr.prev.next = node
            curr.prev = node
            self.head = node
            self.size += 1
            return True
        return False
        

    def insertLast(self, value: int) -> bool:
        node = Node(value)
        # print(node.val)
        if self.size ==0:
            self.head = node
            node.next = node
            node.prev = node
            self.size += 1
            return True
        elif self.size >= self.k:
            return False
        else:
            curr = self.head
            for i in range(self.size-1):
                curr = curr.next
            
            node.next = curr.next
            node.prev = curr
            curr.next.prev = node
            curr.next = node         
            self.size += 1
            curr = self.head
            return True
        return False

    def deleteFront(self) -> bool:
        if self.head is None:
            return False
        elif self.size == 1:
            self.head = None
            self.size -= 1
            return True
        else:
            curr = self.head.next
            curr.prev = self.head.prev
            self.head.prev.next = curr
            self.size -= 1
            self.head = curr
            return True
        return False
        

    def deleteLast(self) -> bool:
        if self.head is None:
            return False
        elif self.size == 1:
            self.head = None
            self.size -= 1
            return True
        else:
            curr = self.head
            for i in range(self.size-2):
                curr = curr.next
            curr.next = curr.next.next
            curr.next.prev = curr
            self.size -= 1
            return True
        return False        

    def getFront(self) -> int:
        if self.head is None:
            return -1
        else:
            curr = self.head
            return curr.val
        return -1       
        

    def getRear(self) -> int:
        curr = self.head
        if self.head is None:
            return -1
        else:            
            for i in range(self.size-1):
                curr = curr.next
            
            return curr.val

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        else:
            return False
        

    def isFull(self) -> bool:
        if self.size == self.k:
            return True
        else:
            return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()