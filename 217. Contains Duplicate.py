#Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
class solution(object):
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        if len(nums) == 1 or k == 0: return False

        numsSet = set(nums)
        if len(numsSet) == len(nums): return False


        for index in range(len(nums)):
            for i in range(index+1,len(nums),1):
                if i-index <= k and nums[index]==nums[i]: return True