#validate if a sudoku is correct

class solution(object):
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            numsMap = {}
            for c in board[i]:
                if c in numsMap.keys() and c != '.' : return False
                else: numsMap[c] = True
                    
        
        for j in range(9):
            numsMap = {}
            for k in range(9):
                c = board[k][j]
                if c in numsMap.keys() and c!= '.' : return False
                else: numsMap[c] = True
        
        numsMap = {}
        for i in range(3):
            for j in range(0,3):
                c = board[i][j]
                if c in numsMap.keys() and c!= '.' : return False
                else: numsMap[c] = True
                    
        numsMap = {}
        for i in range(3):
            for j in range(3,6):
                c = board[i][j]
                if c in numsMap.keys() and c!= '.' : return False
                else: numsMap[c] = True
                #print(numsMap.keys())
                
        numsMap = {}
        for i in range(3):
            for j in range(6,9):
                c = board[i][j]
                if c in numsMap.keys() and c!= '.' : return False
                else: numsMap[c] = True
        
        numsMap = {}
        for i in range(3,6):
            for j in range(0,3):
                c = board[i][j]
                if c in numsMap.keys() and c!= '.' : return False
                else: numsMap[c] = True
                    
        numsMap = {}
        for i in range(3,6):
            for j in range(3,6):
                c = board[i][j]
                if c in numsMap.keys() and c!= '.' : return False
                else: numsMap[c] = True
                    
        numsMap = {}
        for i in range(3,6):
            for j in range(6,9):
                c = board[i][j]
                if c in numsMap.keys() and c!= '.' : return False
                else: numsMap[c] = True
                    
        numsMap = {}
        for i in range(6,9):
            for j in range(0,3):
                c = board[i][j]
                if c in numsMap.keys() and c!= '.' : return False
                else: numsMap[c] = True
                    
        numsMap = {}
        for i in range(6,9):
            for j in range(3,6):
                c = board[i][j]
                if c in numsMap.keys() and c!= '.' : return False
                else: numsMap[c] = True
                    
        numsMap = {}
        for i in range(6,9):
            for j in range(6,9):
                c = board[i][j]
                if c in numsMap.keys() and c!= '.' : return False
                else: numsMap[c] = True
                

        
        return True

#with hashMaps (dicts)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        numsMapHor = {}
        numsMapVer = {}
        numsMapCua = {}
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                print(i,j,num)
                if num != '.':
                    #comprobación líneas
                    if i in numsMapHor.keys():
                        if num in numsMapHor[i] : return False
                        else: numsMapHor[i].append(num)
                    else: numsMapHor[i] = [num]
                        
                    #comprobación columnas
                    if j in numsMapVer.keys():
                        if num in numsMapVer[j] : return False
                        else: numsMapVer[j].append(num)
                    else: numsMapVer[j] = [num]
                    
                    #comprobación cuadrados
                    if (i//3,j//3) in numsMapCua.keys():
                        if num in numsMapCua[i//3,j//3]: return False
                        else: numsMapCua[i//3,j//3].append(num)
                    else: numsMapCua[i//3,j//3] = [num]
                    
        return True