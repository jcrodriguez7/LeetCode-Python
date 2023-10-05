# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    #My solution with two pointers
    def detectCycle(self, head: [ListNode]) -> [ListNode]:
        if head == None or head.next == None: return None
        
        pointer0 = head
        
        seenBy0 = set()
        
        while pointer0:
            if pointer0 in seenBy0: return pointer0
            elif pointer0.next in seenBy0: return pointer0.next
            
            seenBy0.add(pointer0)
            if pointer0.next == None: return None
            pointer0 = pointer0.next.next

    #My solution with one pointer
    def detectCycle(self, head: [ListNode]) -> [ListNode]:
       if head == None or head.next == None: return None
       
       pointer0 = head
       
       seenBy0 = set()
       
       while pointer0:
           if pointer0 in seenBy0: return pointer0
           elif pointer0.next in seenBy0: return pointer0.next
           
           seenBy0.add(pointer0)
           if pointer0.next == None: return None
           seenBy0.add(pointer0.next)
           pointer0 = pointer0.next.next


    #Solution copied from leetcode  Time O(N) Space O(1)    
    def detectCycle(self, head: ListNode) -> ListNode:
        # Initialize two pointers, slow and fast, to the head of the linked list.
        slow = head
        fast = head

        # Move the slow pointer one step and the fast pointer two steps at a time through the linked list,
        # until they either meet or the fast pointer reaches the end of the list.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # If the pointers meet, there is a cycle in the linked list.
                # Reset the slow pointer to the head of the linked list, and move both pointers one step at a time
                # until they meet again. The node where they meet is the starting point of the cycle.
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

        # If the fast pointer reaches the end of the list without meeting the slow pointer,
        # there is no cycle in the linked list. Return None.
        return None