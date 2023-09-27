#Return the index of first unique char in a string. If none, return -1
class solution(object):
    def firstUniqChar(self, s: str) -> int:
        lettersPro = []
        t = s
        
        for i in s:
            t = s.replace(i,"",1)
            if i in lettersPro or i in t:
                t = t.replace(i,"",1)
            else: return s.index(i)
        
        return -1
    #con hashMap
    def firstUniqChar(self, s: str) -> int:
        lettersOcurr = {}
        
        for i in s:
            if i in lettersOcurr:
                lettersOcurr[i] = lettersOcurr[i] + 1
            else: lettersOcurr[i] = 1
            
        if 1 not in lettersOcurr.values(): return -1
        else:
            for char in lettersOcurr.keys():
                if lettersOcurr[char] == 1: return s.index(char)
        return -1