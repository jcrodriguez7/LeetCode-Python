# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        seenNodes = []
        curr = head
        size = 0
        while curr:
            seenNodes.append(curr)
            size += 1
            curr = curr.next
            
        if size == 1: return
        if size == n: return head.next
        
        seenNodes[-n-1].next = seenNodes[-n].next
        return head
    
    #Solución en una pasada, copiada de leetcode
    
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        slow = head
        # advance fast to nth position
        for i in range(n):
            fast = fast.next
            
        if not fast:
            return head.next
        # then advance both fast and slow now they are nth postions apart
        # when fast gets to None, slow will be just before the item to be deleted
        while fast.next:
            slow = slow.next
            fast = fast.next
        # delete the node
        slow.next = slow.next.next
        return head