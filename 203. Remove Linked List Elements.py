# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: [ListNode], val: int) -> [ListNode]:
        
        if head == None: return None
        
        while head.val == val:
            if head.next: head = head.next
            else: return None
            
        curr = head
        
        while curr.next :
            if curr.next.val == val:
                curr.next = curr.next.next
            else: curr = curr.next
            
        return head
        