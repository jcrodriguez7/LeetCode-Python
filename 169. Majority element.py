
#Given an array of nums, return the one that appears at least n/2 times, where n is the length of the array.
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        set_num = set(nums)
        for num in set_num:
            if nums.count(num) > len(nums)/2: return num