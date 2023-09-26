

class Solution(object):

    # ----------------Detecta si en la lista, hay dos números que suman "target" y devuelve sus indices. Existe solución y solo existe 1.----------------

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        # Build the hash table
        for i in range(n):
            numMap[nums[i]] = i

        # Find the complement
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]

        return []  # No solution found
    

    #--------------------------------------------------Traduce de números romanos a numeros "normales" -------------------------------------------
    def romanToInt(self, s: str) -> int:
        solution = 0


        if "IV" in s: 
            solution += 4
            s = s.replace("IV"," ")
        if "IX" in s: 
            solution += 9
            s = s.replace("IX","")
        if "XL" in s:
            solution += 40
            s = s.replace("XL","")
        if "XC" in s:
            solution += 90
            s = s.replace("XC","")
        if "CD" in s:
            solution += 400
            s = s.replace("CD","")
        if "CM" in s:
            solution += 900
            s = s.replace("CM","")
            

        for i in s:
            if i == "I": solution += 1
            elif i == "V": solution += 5
            elif i == "X": solution += 10
            elif i == "L": solution += 50
            elif i == "C": solution += 100
            elif i == "D": solution += 500
            elif i == "M": solution += 1000


        return solution
    
    def romanToInt2(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number


    #--------------------------------------------Detecta cual es el prefijo más largo que comparten TODOS los string de la lista -------------------------------------
    # Ordena la lista, pues estando ordenada, el primer y último elemento son los más diferentes y los que tendrán el prefijo más corto
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans=""
        v=sorted(v)
        first=v[0]
        last=v[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 

    # ----------------------------------------Problema que detecta, en un string, si hay paréntesis, corchetes o llaves bien abiertos y cerrados. -----------------------------
    # () bien, (]) mal, ] mal, ([{}]) bien

	def isValid(self, s: str) -> bool:

        if len(s) % 2: return False

        # Create a pair of opening and closing parrenthesis...
        opcl = dict(('()', '[]', '{}'))
        # Create stack data structure...
        stack = []
        # Traverse each charater in input string...
        for idx in s:
            # If open parentheses are present, append it to stack...
            if idx in '([{':
                stack.append(idx)
            # If the character is closing parentheses, check that the same type opening parentheses is being pushed to the stack or not...
            # If not, we need to return false...
            elif len(stack) == 0 or idx != opcl[stack.pop()]:
                return False
        # At last, we check if the stack is empty or not...
        # If the stack is empty it means every opened parenthesis is being closed and we can return true, otherwise we return false...
        return len(stack) == 0
    

    #-----------------Combina dos listas ordenadas, resultando en 1 ordenada. Se hace empalmando elementos, no vale crear lista total y ordenarla:
    # Definition for singly-linked list.
    class ListNode:
         def __init__(self, val=0, next=None):
             self.val = val
             self.next = next
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        result= ListNode()

        # Si alguna o ambas listas están vacías
        if list1 == None:
            if list2 == None : return None
            else: return list2
        elif list2 == None : return list1

        # Si ambas listas tienen elementos
        if list1.val <= list2.val: 
            result.val = list1.val
            result.next = self.mergeTwoLists(list1.next,list2)
        else: 
            result.val = list2.val
            result.next = self.mergeTwoLists(list1,list2.next)
        
        return result

        #--------------------Elimina duplicados y devuelve k= nº de elementos únicos y sobreescribe la lista con los k primeros numeros, siendo esos k, los k elementos únicos-------
        def removeDuplicates(self, nums: List[int]) -> int:
            lastN = nums[len(nums)-1]
            i = nums[0]
            count = 0
            for num in nums:
                if i == lastN: 
                    nums[count]=i
                    return count + 1
                
                elif num == i: 
                    nums.pop(count)
                    nums.insert(count,i)
                    count  += 1
                    i += 1
                elif num>i:
                    nums.pop(count)
                    nums.insert(count,num)
                    count += 1
                    i = num+1
            return count
	
#------------------------------ Sumar 1 a un número guardado como una listas de int----------------------------------------
def plusOne(self, digits: List[int]) -> List[int]:
        
        sum = 0

        if digits[-1] < 9 : 
            digits[-1] += 1
            return digits

        else:
            digits[-1] = 0
            sum = 1
            for i in range(-2,-len(digits)-1,-1):
                if digits[i] == 9:
                    digits[i] = 0
                    sum = 1
                else: 
                    print("else 8")
                    digits[i] += 1
                    sum = 0
                    break

        if sum==1: 
            return [1] + digits
        return digits    

    #----------------------------------SQRT ---------------------------------------------
    def mySqrt(self, x: int) -> int:
        
        if x == 0: return 0
        if x == 1: return 1

        sol = 1

        for i in range (1,x+1,1):
            if i*i == x: return i
            if i*i > x: return i-1

#---- Para una escalera de n escalones, pudiendo dar pasos de 1 o 2 escalones, dar las opciones que existen de completar la escalera
def climbStairs(self, n: int) -> int:
        memo = {}
        return self.helper(n, memo)
    
    def helper(self, n: int, memo: dict[int, int]) -> int:
        if n == 0 or n == 1:
            return 1
        if n not in memo:
            memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo)
        return memo[n]
#-------------- Ordena dos listas de int, m y n, y la resultante la guarda en m.
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        if m == 0 : 
            nums1.clear()
            nums1 += nums2

        elif n != 0 :
            i = 0
            j= 0

            supp = nums1.copy()

            for x in range(n+m):                    
                if (j == n) or (supp[i] <= nums2[j] and i<m): 
                    nums1[x] = supp[i]
                    i += 1
                else:
                    nums1[x] = nums2[j]
                    j += 1

def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    while n > 0:
        if nums1[m-1] >= nums2[n-1] and m>0:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1

#-----------------inorder Traversal de un árbol -------------------------------
#recursivo
def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if root == None: return []
        if root.left == None and root.right == None: return [root.val]


        def recInorderTraversal(root: [TreeNode]) -> List[int]:
            result = []
            if root.left : result = result + recInorderTraversal(root.left)
            result.append(root.val)
            if root.right : result = result + recInorderTraversal(root.right)
            return result
        
        return recInorderTraversal(root)
#iterativo
def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st = []
        res = []

        while root or st:
            while root:
                st.append(root)
                root = root.left
            
            root = st.pop()
            res.append(root.val)

            root = root.right
        
        return res   

#------------------Saber si un árbol es simétrico--------------------------
# Mi solución
def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        position1= []        
        position2= []
        def recLeft(root: [TreeNode]) -> List[int]:
            result = []
            if root.left : 
                position1.append("left")
                result = result + recLeft(root.left)
            result.append(root.val)
            if root.right : 
                position1.append("right")
                result = result + recLeft(root.right)
            return result

        def recRight(root: [TreeNode]) -> List[int]:
            result = []

            if root.right : 
                position2.append("left")
                result = result + recRight(root.right)
            result.append(root.val)
            if root.left : 
                position2.append("right")
                result = result + recRight(root.left)
            return result

        leftSide = recLeft(root)
        rightSide = recRight(root)
        print(str(position1) + str(position2))
        if leftSide == rightSide and position1 == position2: return True
        else: return False

def isSymmetric(self, root):
        # Special case...
        if not root:
            return True;
        # Return the function recursively...
        return self.isSame(root.left, root.right)
    # A tree is called symmetric if the left subtree must be a mirror reflection of the right subtree...
    def isSame(self, leftroot, rightroot):
        # If both root nodes are null pointers, return true...
        if leftroot == None and rightroot == None:
            return True
        # If exactly one of them is a null node, return false...
        if leftroot == None or rightroot == None:
            return False
        # If root nodes haven't same value, return false...
        if leftroot.val != rightroot.val:
            return False
        # Return true if the values of root nodes are same and left as well as right subtrees are symmetric...
        return self.isSame(leftroot.left, rightroot.right) and self.isSame(leftroot.right, rightroot.left)

#--------------------------------------Retorna un reverse String, algoritmo in place ---------------------------
def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range((len(s))//2):
            aux = s[i]
            s[i]=s[len(s)-i-1]
            s[len(s)-i-1] = aux

    #solución TOP
def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]

#----------------------------Devuelve la profundida de un árbol-----------------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root== None: return 0
        if root.right==None and root.left==None: return 1
        def recMaxDepth(root: Optional[TreeNode]) -> int:
            if root==None: return 0

            if root.right==None and root.left==None: return 1
            
            return 1 + max(recMaxDepth(root.left),recMaxDepth(root.right))
        
        return 1 + max(recMaxDepth(root.left),recMaxDepth(root.right))

#-----------------Crear n filas del triángulo de Pascal ------------------------------
def generate(self, numRows: int) -> List[List[int]]:
        
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

#----------------------Reverse binary 32-bit number--------------------------
def reverseBits(self, n: int) -> int:
        resultString = ""
        while(n>1):
            resultString += str(n%2)
            n = n // 2
        resultString += str(n)

        while len(resultString) < 32:
            resultString += str(0)

        result = 0
        powIndex = 31
        for i in resultString:
            result += int(i)*(2**powIndex)
            powIndex -= 1
        return result
    #top version
def reverseBits(self, n: int) -> int:
    # Initialize the reversed number to 0
    reversed_num = 0
    
    # Iterate over all 32 bits of the given number
    for i in range(32):
        # Left shift the reversed number by 1 and add the last bit of the given number to it
        reversed_num = (reversed_num << 1) | (n & 1)
        # To add the last bit of the given number to the reversed number, perform an AND operation with the given number and 1
        n >>= 1
    
    # Return the reversed number
    return reversed_num

#------------------ Recibe dos listas con n elementos cada una, que conforman un nº ordenado al revés. Retornar la suma de los dos números
# [1,2,4] y [2,3] retorna [3,5,4]
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        finalSum = ListNode()
        currNode = finalSum
    
        while((l1 != None) or (l2 != None)):
            print(l1,l2,finalSum,currNode)
            currSum = currNode.val
           
            if l1 != None: currSum += l1.val
            if l2 != None: currSum += l2.val

            left = currSum % 10
            currNode.val = left
            if currSum >9: 
                print("next 1")
                currNode.next = ListNode(1)
            elif (l1 and l1.next) or (l2 and l2.next) : 
                currNode.next = ListNode(0)

            currNode = currNode.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        
        return finalSum

#------------------------ Happy number ----------------- anotación corta, codigo corto, simple

def isHappy(self, n: int) -> bool:
    past = set()
    while n != 1:
        n = sum(int(i)**2 for i in str(n))
        if n in past: return False
        past.add(n)
    
    return True

#------------------------ Isomorphic words--------------------
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

#-------------Devolver lista con elementos repetidos en ambas listas(input) y con el menor indice combinado
def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
                       
        indexWordMap = {}
        
        for word in list1:
            if word in list2:
                indexSum = list1.index(word) + list2.index(word)
                
                if indexSum in indexWordMap:
                    indexWordMap[indexSum] = indexWordMap.get(indexSum) + [word]
                else:
                    indexWordMap[indexSum] = [word]
                

        minKey = min(indexWordMap.keys())
 
        return indexWordMap.get(minKey)

#-------------devolver index de la primera letra que no se repita dentro de un string, si se repiten todas, -1
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
#retornar intersección de elementos de dos listas. Los elementos en la intersección han de estar tantas veces presentes como se interseccionen
def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        map1 = {}
        map2 = {}
                
        for i in nums1:
            if i not in map1: map1[i]=1
            else: map1[i] += 1
                
        for j in nums2:
            if j not in map2: map2[j]=1
            else: map2[j] += 1
        
        inter = []
        
        
        for k in map1.keys():
            if k in map2:
                times = min(map1[k],map2[k])
                for t in range(times): inter.append(k)
       
                
        return inter

#Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        if len(nums) == 1 or k == 0: return False

        numsSet = set(nums)
        if len(numsSet) == len(nums): return False


        for index in range(len(nums)):
            for i in range(index+1,len(nums),1):
                if i-index <= k and nums[index]==nums[i]: return True

            
# Agrupar los anagramas:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
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

#valid sudoku
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

#con hashMaps (diccionarios)
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

  #------------encontrar subtress duplicados--------------------- (copio de leetcode, no me sale)
  def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        
        seen = collections.defaultdict(int)
        res = []
        
        def helper(node):
            if not node:
                return
            sub = tuple([helper(node.left), node.val, helper(node.right)])
            if sub in seen and seen[sub] == 1:
                res.append(node)
            seen[sub] += 1
            return sub
        
        helper(root)
        return res

# stones and jewels. retorna el número de piedras que son joyas.
def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        
        count=0
                
        for i in stones:
            if i in jewels: count+=1
                
        return count

#copiado - con set, que va más rápido
 def numJewelsInStones(self, J: str, S: str) -> int:
        counter = 0
        jewels = set(J) # search in a set is instant - O(1)
        for stone in S:
            if stone in jewels:
                counter += 1
        return counter

#  Longest Substring Without Repeating Characters
# mía
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
#con window y map
def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        output = 0
        for r in range(len(s)):
            '''
            If s[r] not in seen, we can keep increasing the window size by moving right pointer
            '''
            if s[r] not in seen:
                output = max(output,r-l+1)
            '''
            There are two cases if s[r] in seen:
            case1: s[r] is inside the current window, we need to change the window by moving left pointer to seen[s[r]] + 1.
            case2: s[r] is not inside the current window, we can keep increase the window
            '''
            else:
                if seen[s[r]] < l:
                    output = max(output,r-l+1)
                else:
                    l = seen[s[r]] + 1
            seen[s[r]] = r
        return output

# 4 sum ii, copiado
def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n, hm, res = len(nums1), defaultdict(int), 0

        for i in range(n):
            for j in range(n):
                hm[nums1[i] + nums2[j]] += 1 

        
        for k in range(n):
            for l in range(n):
                res += hm[0 - (nums3[k] + nums4[l])]

        return res    


#top k frequent elements
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if len(nums) <= k: return nums
        
        if len(nums) == len(set(nums)): return[nums[0],nums[1]]
        
        counts = {}
        
        for n in nums:
            if n in counts: counts[n] += 1
            else: counts[n] = 1
                
        counts = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))
        
        result = list(counts.keys())[:k]
    
        return result