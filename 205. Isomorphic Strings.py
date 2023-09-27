#Returns True if two strings are isomorphic
class solution(object):
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)): return False
        hash_map = {}
        for index in range(len(t)):
            if t[index] not in hash_map.keys():
                hash_map[t[index]] = s[index]
                print(hash_map)
            elif hash_map[t[index]] != s[index]:
                return False
        
        return True