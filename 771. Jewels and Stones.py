#Stones and jewels. Return how many stones are jewels
class solution(object):

    def numJewelsInStones(self, jewels: str, stones: str) -> int:
                
        count=0
                
        for i in stones:
            if i in jewels: count+=1
                
        return count

#Copied form leetcode - With set, resolves faster as search is O(1) instead of O(n)
    def numJewelsInStones(self, J: str, S: str) -> int:
        counter = 0
        jewels = set(J) # search in a set is instant - O(1)
        for stone in S:
            if stone in jewels:
                counter += 1
        return counter