
#Implementing a Linked List class with its Node class.

class Node:
        
        def __init__(self,val=0):
            self.val = val
            self.next = None

class MyLinkedList:
    
    
        
    
    def __init__(self):
        self.head = None
        self.length = 0
        
    def get(self, index: int) -> int:
        
        if index >= self.length: return -1
        
        x = self.head

        while(index > 0):
            x = x.next
            index -= 1
        return x.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)
        

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.length,val)

    def addAtIndex(self, index: int, val: int) -> None:
        
        if index > self.length:
            return

        current = self.head
        new_node = ListNode(val)

        if index == 0:
            new_node.next = current
            self.head = new_node
        else:
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

        self.length += 1
        
            

    def deleteAtIndex(self, index: int) -> None:
        
        if index < self.length:
            if index == 0: self.head = self.head.next
            else:
                x = self.head
                while(index > 1):
                    x = x.next
                    index -= 1
                x.next = x.next.next
            self.length-=1