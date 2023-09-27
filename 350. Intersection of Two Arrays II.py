
# Return the intersection of two int lists. Items in common list, must appear as many times as it shows in given lists. 
class solution(object):    
    def intersect(self, nums1: [int], nums2: [int]) -> [int]:
        
        map1 = {}
        map2 = {}
                
        for i in nums1:
            if i not in map1: map1[i]=1
            else: map1[i] += 1
                
        for j in nums2:
            if j not in map2: map2[j]=1
            else: map2[j] += 1
        
        inter = []
        
        
        for k in map1.keys():
            if k in map2:
                times = min(map1[k],map2[k])
                for t in range(times): inter.append(k)
       
                
        return inter
