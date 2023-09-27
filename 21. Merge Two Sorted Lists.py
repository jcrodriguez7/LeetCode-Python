
# It combines two ordered lists, giving 1 ordered list. The list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class solution(object):
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        result= ListNode()

        # If any or both lists are empty
        if list1 == None:
            if list2 == None : return None
            else: return list2
        elif list2 == None : return list1

        # If both lists have items
        if list1.val <= list2.val: 
            result.val = list1.val
            result.next = self.mergeTwoLists(list1.next,list2)
        else: 
            result.val = list2.val
            result.next = self.mergeTwoLists(list1,list2.next)
        
        return result