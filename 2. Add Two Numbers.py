# It gets 2 n-listNode lists. Each list is a reversed number. Return the sum of both lists.
# 
# [1,2,4] + [2,3] retorna [3,5,4]

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class solution(object):
     
    def addTwoNumbers(self, l1: [], l2: []) -> []:

        #FinalSum is the returned Node conforming the result sum
        #currNode is an iterator over finalSum ListNodes
        finalSum = ListNode()
        currNode = finalSum
    
        while((l1 != None) or (l2 != None)):
            currSum = currNode.val
            
            #If there is nodes left in any list:
            if l1 != None: currSum += l1.val
            if l2 != None: currSum += l2.val

            left = currSum % 10
            currNode.val = left

            #If there is carry, we initialize next ListNode = 1
            if currSum >9: 
                currNode.next = ListNode(1)
            elif (l1 and l1.next) or (l2 and l2.next) : 
                currNode.next = ListNode(0)

            currNode = currNode.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        
        return finalSum