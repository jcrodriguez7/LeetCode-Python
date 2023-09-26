class solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) <=1: return len(s)
        leftP = 0
        rightP = 1
        
        currentMax = 1
        currentWord = s[0]
        
        while rightP < len(s):

            if not s[rightP] in currentWord:
                currentWord = s[leftP:rightP+1]
                rightP += 1
                if len(currentWord) > currentMax : currentMax = len(currentWord)
                
            else:
                leftP = s.index(s[rightP],leftP,len(s))+1
                currentWord = s[leftP:rightP+1]
                rightP +=1
        
        return currentMax
    
    # Window algorith and map
    def lengthOfLongestSubstring(self, s: str) -> int:
            seen = {}
            l = 0
            output = 0
            for r in range(len(s)):
                '''
                If s[r] not in seen, we can keep increasing the window size by moving right pointer
                
                There are two cases if s[r] in seen:
                case1: s[r] is inside the current window, we need to change the window by moving left pointer to seen[s[r]] + 1.
                case2: s[r] is not inside the current window, we can keep increase the window
                '''
                if s[r] not in seen:
                    output = max(output,r-l+1)
                
                else:
                    if seen[s[r]] < l:
                        output = max(output,r-l+1)
                    else:
                        l = seen[s[r]] + 1
                seen[s[r]] = r
            return output