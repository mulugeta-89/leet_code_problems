class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
    def getSize(self):
        size = 0
        current = self.head
        while(current):
            size += 1
            current = current.next
        return size
    def get(self, index):
        if index > self.getSize()-1:
            return -1
        currentNode = self.head
        if index == 0:
            return self.head.val
        else:
            for i in range(index):
                currentNode = currentNode.next
            return currentNode.val
    def addAtHead(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
    def addAtTail(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_node
    def addAtIndex(self, index, val):
        if index > self.getSize():
            return
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        elif index == self.getSize():
            self.addAtTail(val)
        else:
            current = self.head
            for i in range(index-1):
                current = current.next
            the_other = current.next
            current.next = new_node
            new_node.next = the_other
    def deleteAtIndex(self, index):
        if index > self.getSize()-1:
            return
        current = self.head
        if index == 0:
            self.head = current.next
            current = None
        else:
            for i in range(index):
                prev = current
                current = current.next
            prev.next = current.next
            current = None
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)