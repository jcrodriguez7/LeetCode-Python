# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#Iterative version
class Solution:
    #
    def reverseList(self, head: [ListNode]) -> [ListNode]:
        if head == None or head.next == None: return head
        
        lastMoved = None
        firstHead = head
        
        while firstHead.next != None:
            lastMoved = firstHead.next
            firstHead.next = lastMoved.next
            lastMoved.next = head
            head = lastMoved
        return head
        

            
            


