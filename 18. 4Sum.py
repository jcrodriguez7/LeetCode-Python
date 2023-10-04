class Solution:
    #solución mía, no vale para todos los ejemplos, para los test con listas muy grandes, salta Time Limit Exceeded
    def fourSum(self, nums: [int], target: int) -> [[int]]:
        
        result = []

        def twoSum(numsSec: [int], targetSec: int) -> [[int]]:
            resultSec = []
            for i in numsSec:
                partNumsSec = numsSec.copy()
                partNumsSec.remove(i)
                if targetSec-i in partNumsSec:
                    resultSec.append([i,targetSec-i])
                    numsSec.remove(i)
                    numsSec.remove(targetSec-i)
            return resultSec
        
        for i in nums:
            partNums = nums.copy()
            partNums.remove(i)
            for j in partNums:
                partNumsSec = partNums.copy()
                partNumsSec.remove(j)     
                
                twoSumResult = twoSum(partNumsSec,target-i-j)
                    
                for k in twoSumResult:
                        k.append(i)
                        k.append(j)
                        k = sorted(k)
                        if k not in result:
                            result.append(k)
                    
        return result

    #Copiado de soluciones de leetcode
    def fourSum(self, nums: [int], target: int) -> [[int]]:
        ans = set()
        n = len(nums)
        nums.sort()
        for i in range(n):
            for j in range(i+1,n):
                left = j + 1
                right = n - 1

                while left < right:
                    total = nums[i] + nums[left] + nums[right]+nums[j]
                    if total > target:
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        ans.add(tuple(sorted((nums[i], nums[left], nums[right],nums[j]))))
                    
                        left += 1
                        right -= 1
        return ans