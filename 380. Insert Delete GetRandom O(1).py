
#RandomizedSet coding

import random
class RandomizedSet:
    
   
    
    def __init__(self):
        self.ownSet = set()
    
    def insert(self, val: int) -> bool:
        if val in self.ownSet : return False
        self.ownSet.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.ownSet: return False
        self.ownSet.discard(val)
        return True
        

    def getRandom(self) -> int:
        
        result = random.choice(list(self.ownSet))
        return result
    
#Good one. O(1) in getRandom.
#Having only a set, in getRandom we need to convert the set to a list, which adds a lot of time to the function.
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashTable = {}
        self.arr = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.hashTable:
            self.hashTable[val] = len(self.arr)
            self.arr.append(val)
            return True
        
        return False
        
        
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.hashTable:
        
            self.hashTable[self.arr[-1]] = self.hashTable[val]
            self.arr[self.hashTable[val]] = self.arr[-1]

            self.arr.pop()
            self.hashTable.pop(val)
            
            return True
        
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.arr)