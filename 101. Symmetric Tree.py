#Decide if a tree is symmetric
#My solution
class solution(object):
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

    #Copied solution, a more clear one.
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