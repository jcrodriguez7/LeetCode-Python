# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    #Mía, Time O(n+m), Space O(n)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        visitedNodes = set()

        while headA:
            visitedNodes.add(headA)
            headA = headA.next

        while headB:
            if headB in visitedNodes: return headB
            headB = headB.next
        return 

    #La mejor, Time O(n+m), Space O(1)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        one = headA
        two = headB

        while one != two:
            one = headB if one is None else one.next
            two = headA if two is None else two.next
        return one
        