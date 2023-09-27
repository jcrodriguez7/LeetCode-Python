#Add 1 to a number stored as a list of ints

class solution(object):
     
    def plusOne(self, digits: [int]) -> [int]:
        
        sum = 0
        #If last digit is less than 9, just add 1.
        if digits[-1] < 9 : 
            digits[-1] += 1
            return digits

        #If last number is 9, we have to carry 1 to previous digit
        else:
            digits[-1] = 0
            sum = 1
            for i in range(-2,-len(digits)-1,-1):
                #If there is carry:
                if digits[i] == 9:
                    digits[i] = 0
                    sum = 1
                
                else: 
                    digits[i] += 1
                    sum = 0
                    break

        if sum==1: 
            return [1] + digits
        return digits    
