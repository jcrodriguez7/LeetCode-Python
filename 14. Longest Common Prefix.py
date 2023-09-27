
#Returns the longest common prefix between all the string in given list.
class solution(object):    
    def longestCommonPrefix(self, v: [str]) -> str:
        ans=""

        #We order the list, so that way, first and last items will be the most different between each other and their prefix will be the shorter.
        v=sorted(v)
        first=v[0]
        last=v[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 