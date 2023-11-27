'''Given an integer n, return a string array answer (1-indexed) where:

    answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    answer[i] == "Fizz" if i is divisible by 3.
    answer[i] == "Buzz" if i is divisible by 5.
    answer[i] == i (as a string) if none of the above conditions are true.
'''



class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1,n+1):
            if i % 3 == 0:
                if i % 5 == 0:
                    res.append("FizzBuzz")
                else: res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        
        return res
    

    #Fastest version from leecode, not using %, that takes longer. It's probably faster for small arrays, it will probably take longer with long arrays cause it'll be O(n)*4 instead of O(n)*O(%)
    '''  def fizzBuzz(self, n: int) -> List[str]:
        f, b, fb = 'Fizz', 'Buzz', 'FizzBuzz'
        arr = [str(x + 1) for x in range(n)]
        
        for i in range(2, n, 3):
            arr[i] = f
        
        for i in range(4, n, 5):
            arr[i] = b
        
        for i in range(14, n, 15):
            arr[i] = fb
        
        return arr
    '''