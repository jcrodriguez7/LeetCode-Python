#Returns n rows of a Pascal's triangle
#In Pascal's triangle, each number is the sum of the two numbers directly above it
class solution(object):
    def generate(self, numRows: int) -> [[int]]:
        
        resultList = [[1]]

        if numRows == 1: return resultList
        
        previousRow = [1,1]
        for i in range (1,numRows):
            currentRow = [1,1]
            for j in range(1,i):
                currentRow.insert(j,(previousRow[j-1]+previousRow[j]))
                
            resultList.append(currentRow)
            previousRow = currentRow.copy()

        return resultList