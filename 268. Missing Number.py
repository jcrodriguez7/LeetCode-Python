
'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(x for x in range(0,len(nums)+1)) - sum(nums)


'''
Another solution from leetcode user
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(x for x in range(0,len(nums)+1)) - sum(nums)
'''