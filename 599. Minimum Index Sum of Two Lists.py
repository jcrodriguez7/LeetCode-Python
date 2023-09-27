#Given two arrays of strings list1 and list2, find the common strings with the least index sum.
class solution(object):
    def findRestaurant(self, list1: [str], list2: [str]) -> [str]:
                       
        indexWordMap = {}
        
        for word in list1:
            if word in list2:
                indexSum = list1.index(word) + list2.index(word)
                
                if indexSum in indexWordMap:
                    indexWordMap[indexSum] = indexWordMap.get(indexSum) + [word]
                else:
                    indexWordMap[indexSum] = [word]
                

        minKey = min(indexWordMap.keys())
 
        return indexWordMap.get(minKey)