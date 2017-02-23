class TreeCode:
    
    def __init__(self):
        pass
    
    class TreeNode(object):
         def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

    '''Given a binary tree, find its maximum depth.'''
    def maxDepth(self, root):
        if root == None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    '''Given a binary tree, return the level order traversal of its nodes' values.
     (ie, from left to right, level by level)'''
    def levelOrder(self, root):    
        result = []
        def getSolution(p, index):
            if p == None:
                return
            if len(result) <= index:
                result.append([])
            result[index].append(p.val)
            if p.left:
                getSolution(p.left, index + 1)
            if p.right:
                getSolution(p.right, index + 1)
        getSolution(root, 0)
        return result

    '''Given a binary tree, check whether it is a mirror of itself(ie, symmetric around its center)'''
    def isSymmetric(self, root):  
        def check(left, right):
            def check(left, right):
                if left == None and right == None:
                return True
            elif left == None or right == None:
                return False
            return  left.val == right.val and check(left.left, right.right) and check(left.right, right.left)
        if root == None:
            return True
        return check(root.left, root.right)
        if root == None:
            return True
        return check(root.left, root.right)
            



        
     
   
        
        
        
            


        
    