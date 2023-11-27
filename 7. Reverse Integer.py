'''Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.'''

class Solution:
    def reverse(self, x: int) -> int:
        
        neg = False
        if x < 0 : neg = True

        x = abs(x) #delete '-' sign
        listDigits = [x for x in str(x)] #convert number to list of chars
        
        listDigits = listDigits[::-1] #reverse
        reversedNumber = ''.join(listDigits) #join into string
        reversedNumber = int(reversedNumber) #convert to int

        if neg: reversedNumber = -reversedNumber #if x was negative when passed, get the sign back
        if reversedNumber < (-(pow(2,31))) or reversedNumber > pow(2,31): return 0 #if it is out of bound, return 0
        else: return reversedNumber

        