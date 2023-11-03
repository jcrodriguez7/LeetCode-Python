import string
'''
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
'''

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        index = len(columnTitle) - 1
        result = 0
        columnTitle = columnTitle.lower()
        for l in columnTitle:
            result += (string.ascii_lowercase.index(l) + 1) * (26**index)
            index -= 1
        return result