# Group anagrams:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
class solution(object):
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        groupWords = [[""]]
        if len(strs) == 0 : return groupWords
        if len(strs) == 1 : return [strs]
        
        groupWordsMap = {}
            
        for word in strs:
            sortedWord = ''.join(sorted(word))
            
            if sortedWord not in groupWordsMap:
                groupWordsMap[sortedWord] = [word]
            else: groupWordsMap[sortedWord].append(word)
                        
        return list(groupWordsMap.values())