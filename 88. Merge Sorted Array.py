#Merge two lists, resulting in a in-place modify of the first given list. Don't return anything.

class solution(object):
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        
        if m == 0 : 
            nums1.clear()
            nums1 += nums2

        elif n != 0 :
            i = 0
            j= 0

            supp = nums1.copy()

            for x in range(n+m):                    
                if (j == n) or (supp[i] <= nums2[j] and i<m): 
                    nums1[x] = supp[i]
                    i += 1
                else:
                    nums1[x] = nums2[j]
                    j += 1

    #I got this solution from another user, it is easier.
    def merge2(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        while n > 0:
            if nums1[m-1] >= nums2[n-1] and m>0:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
