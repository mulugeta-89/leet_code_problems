class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyCircularQueue:
    def __init__(self, k: int):
        self.global_size = k
        self.current = 0
        self.head = 0
        self.tail = 0
    def enQueue(self, value):
        if self.isFull():
            return False
        else:
            new_node = Node(value)
            if self.isEmpty():
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = self.tail.next
            self.current += 1
            return True
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = self.head.next
        self.current -= 1
        return True
        
    def Front(self) -> int:
        return self.head.val if not self.isEmpty() else -1
    def Rear(self) -> int:
        return self.tail.val if not self.isEmpty() else -1
    def isEmpty(self) -> bool:
        return self.current == 0
    def isFull(self) -> bool:
        return self.current == self.global_size
        
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()