#Returns a reversed string, in-place.
class solution(object):
        def reverseString(self, s: List[str]) -> None:
                """
                Do not return anything, modify s in-place instead.
                """
                for i in range((len(s))//2):
                aux = s[i]
                s[i]=s[len(s)-i-1]
                s[len(s)-i-1] = aux

        #TOP solution (copied)
        def reverseString(self, s: List[str]) -> None:
                s[:] = s[::-1]