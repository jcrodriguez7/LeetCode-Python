class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        zeroCount = nums.count(0)
        
        for _ in range(zeroCount):
            nums.remove(0)
            nums.append(0)
        """
        Solution from leetcode, 1/3 time of mine, 150ms vs 450ms
        
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            # wait while we find a non-zero element to
            # swap with you
            if nums[slow] != 0:
                slow += 1
        """