import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        s = s.replace(" ","")
        s = s.replace("_","")
        match = re.findall('\w+', s)
                
        if match:
            match = ''.join(match) 
            print(match)
            print(match[::-1])
        return match == match[::-1]