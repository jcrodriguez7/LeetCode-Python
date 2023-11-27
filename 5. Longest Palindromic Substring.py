class Solution:
#----------1st version, recursive--------------------------
    def interiorPalindrome(self,s) -> str:
        if len(s) <= 1 : return True
        if len(s) == 2:
            if s[0]==s[1]: return True
            else: return False
        
        if s[0]==s[-1]: return self.interiorPalindrome(s[1:-1])
        return False




    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1: return s
        if len(s) == 2 and s[0]==s[1]: return s

        pal = s[0]
        for i in range(0,len(s)-1):
            
            if len(pal) >= len(s)-i: break
            j = s.rfind(s[i],i+1)
                            
            while j != -1 and (j-i+1 > len(pal)):
                if i+1==j or self.interiorPalindrome(s[i+1:j]) == True:
                    
                    pal = s[i:j+1]
                    break
                else:
                    j = s.rfind(s[i],i+1,j)

        return pal

    
#--------------2nd version, faster and using less memory-------------------
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1: return s
        if len(s) == 2 and s[0]==s[1]: return s

        pal = s[0]
        for i in range(0,len(s)-1):
            
            if len(pal) >= len(s)-i: break
            j = s.rfind(s[i],i+1)

            while j != -1 and (j-i+1 > len(pal)):
                print(i,j)    
                if (j-i) % 2 == 0: #odd
                    mid = (int)((j-i)/2)
                    
                    if s[i:mid+i] == s[i+mid+1:j+1][::-1]:
                        pal = s[i:j+1]

                    else: j = s.rfind(s[i],i+1,j)

                else: #even
                    mid = (j-i)//2
                    
                    if i+1 == j or s[i:mid+i+1] == s[i+mid+1:j+1][::-1]:
                        pal = s[i:j+1]
                    
                    else: j = s.rfind(s[i],i+1,j)
                

        return pal