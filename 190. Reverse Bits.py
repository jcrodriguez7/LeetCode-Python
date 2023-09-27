#Reverse bits of a given 32 bits unsigned integer.
class solution(object):
    def reverseBits(self, n: int) -> int:
        resultString = ""
        while(n>1):
            resultString += str(n%2)
            n = n // 2
        resultString += str(n)

        while len(resultString) < 32:
            resultString += str(0)

        result = 0
        powIndex = 31
        for i in resultString:
            result += int(i)*(2**powIndex)
            powIndex -= 1
        return result
    

    #top version (copied)
    def reverseBits(self, n: int) -> int:
    # Initialize the reversed number to 0
        reversed_num = 0
        
        # Iterate over all 32 bits of the given number
        for i in range(32):
            # Left shift the reversed number by 1 and add the last bit of the given number to it
            reversed_num = (reversed_num << 1) | (n & 1)
            # To add the last bit of the given number to the reversed number, perform an AND operation with the given number and 1
            n >>= 1
        
        # Return the reversed number
        return reversed_num