#-----------------Binary Tree Inorder Traversal -------------------------------
#Recursive
class solution(object):
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
#Iterative
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