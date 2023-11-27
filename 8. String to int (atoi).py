#Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if(len(s)==0) : return 0
        validDigits = set([str(x) for x in range(0,10)])
        numberFound = False
        l=0
        neg = False
        charDigits = []
        
        while l < len(s):
            
            if s[l] == '0':
                if  not numberFound: 
                    l+=1
                    numberFound = True
                else: 
                    charDigits.append(s[l])
                    l+=1

            elif s[l] in validDigits: 
                numberFound = True
                charDigits.append(s[l])
                l+=1
            
            elif s[l] == '-':
                if not numberFound:
                    numberFound=True
                    neg = True
                    l+=1
                else: break

            elif s[l] == '+':
                if not numberFound: 
                    numberFound = True
                    l+=1
                else: break
            
            else:
                if numberFound: break
                else: return 0
                    
        if len(charDigits)==0: return 0
        
        else: number = int(''.join(charDigits))

        if neg: number = -number


        if number > pow(2,31)-1:  number = pow(2,31)-1
        elif number < -pow(2,31): number = -pow(2,31)
               
        return number