class solution(object):
    '''
    For a given int list "nums", give the "k" numbers that appears with more frequency -
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            
            '''
            Base cases:
            If nums length is < k
            If nums has not repeated items
            '''
            
            if len(nums) <= k: return nums
            
            if len(nums) == len(set(nums)): return[nums[0],nums[1]]
            
            '''
            Frequency of numbers is stored in a dict. Key is the number, frequency the value.
            After going once through the complete list of numbers, order it and return the k first ones.
            '''
            counts = {}
            
            for n in nums:
                if n in counts: counts[n] += 1
                else: counts[n] = 1
                    
            counts = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))
            
            result = list(counts.keys())[:k]
        
            return result