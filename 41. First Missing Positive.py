'''
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
'''
class Solution:

    def firstMissingPositive(self, nums: List[int]) -> int:
        
        if max(nums) < 0 or min(nums)>1: return 1
        dictio = {}

        for i in nums:
            dictio[i] = 1
            
        for i in range(1,max(nums)):
            if i not in dictio.keys(): return i
        return max(nums) + 1