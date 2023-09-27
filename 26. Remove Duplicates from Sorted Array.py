#--------------------Elimina duplicados y devuelve k= nº de elementos únicos y sobreescribe la lista con los k primeros numeros, siendo esos k, los k elementos únicos-------
# Given an int list, removes the duplicates in-place and return the number of unique elements remaining

class solution(object):    
    def removeDuplicates(self, nums: [int]) -> int:
        lastN = nums[len(nums)-1]
        i = nums[0]
        count = 0
        for num in nums:
            if i == lastN: 
                nums[count]=i
                return count + 1
            
            elif num == i: 
                nums.pop(count)
                nums.insert(count,i)
                count  += 1
                i += 1
            elif num>i:
                nums.pop(count)
                nums.insert(count,num)
                count += 1
                i = num+1
        return count