import sys
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
    
    '''Given two binary trees, write a function to check if they are equal or not.'''
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
    '''Given a binary tree, determine if it is height-balanced.'''
    def isBalanced(self, root):
        def getDepth(node):
            if node == None:
                return 0
            leftDepth = getDepth(node.left)
            if leftDepth == -1:
                return -1
            rightDepth = getDepth(node.right)
            if rightDepth == -1:
                return -1
            if abs(leftDepth - rightDepth) > 1:
                return -1
            return max(leftDepth, rightDepth) + 1
        return getDepth(root) != -1
    
    '''Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.'''
    def hasPathSum(self, root, sum):
        if root == None:
            return False
        def loop(node, num):
            if node == None:
                return False
            num += node.val
            if node.left == None and node.right == None:
                return num == sum
            else:
                return loop(node.left, num) or loop(node.right, num)
        return loop(root, 0)
    
    
    '''Given a binary tree, return the preorder traversal of its nodes values.'''
    def preorderTraversal(self, root):
        if root == None:
            return []
        result = []
        stack = [root]
        while len(stack) != 0:
            p = stack[-1]
            result.append(p.val)
            stack.pop()
            if p.right != None:
                stack.append(p.right)
            if p.left != None:
                stack.append(p.left)
        return result
    
    '''Given a binary tree, return the inorder traversal of its nodes' values.'''
    def inorderTraversal(self, root):
        if root == None:
            return []
        result = []
        stack = []
        p = root
        while len(stack) != 0 or p:
            while p != None:
               stack.append(p)
               p = p.left
            if len(stack) != 0:
               p = stack.pop()
               result.append(p.val)
               p = p.right
        return result
    
    '''Given a binary tree, return the postorder traversal of its nodes' values.'''
    def postorderTraversal(self, root):
        if root == None:
            return []
        result = []
        stack = [root]
        pre = None
        while len(stack) != 0:
            p = stack[-1]
            if (p.left == None and p.right == None) or (pre != None and (pre == p.left or pre == p.right)):
                result.append(p.val)
                stack.pop()
                pre = p
            else:
                if p.right:
                    stack.append(p.right)
                if p.left:
                    stack.append(p.left)    
        return result
    
    '''Populate each next pointer to point to its next right node. 
    If there is no next right node, the next pointer should be set to NULL.'''
    class TreeLinkNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
            self.next = None
        
    def connect(self, root):
        if root == None:
            return
        def linkNext(node):
            if node == None:
                return
            if node.left != None:
                node.left.next = node.right
                linkNext(node.left)
            if node.right != None:
                next = None
                if node.next != None and node.next.left != None:
                    node.right.next = node.next.left
                else:
                    node.right.next = None
                linkNext(node.right)
        root.next = None
        linkNext(root)
    
    '''What if the given tree could be any binary tree? 
    Would your previous solution still work?'''
    def connect2(self, root):
        tail = dummy = TreeLinkNode(0)
        node = root
        while node != None:
            tail.next = node.left
            if tail.next:
                tail = tail.next
            tail.next = node.right
            if tail.next:
                tail = tail.next
            node = node.next
            if not node:
                tail = dummy
                node = dummy.next
    
    '''Given a singly linked list where elements are sorted in ascending order.
    convert it to a height balanced BST'''

    class ListNode(object):
        def __init__(self, x):
            self.val = x
            self.next = None
    def sortedListToBST(self, head):
        def sort(start, end):
            if start == end:
                return None
            slow = fast = start
            while fast != end and fast.next != end:
                slow = slow.next
                fast = fast.next.next
            node = TreeNode(slow.val)
            node.left = sort(start, slow)
            node.right = sort(slow.next, end)
        sort(head, None)
    
    '''Given an array where elements are sorted in ascending order, convert it to a height balanced BST.'''
    def sortedArrayToBST(self, nums):
        if len(nums) == 0:
            return None
        midIndex = len(nums) / 2
        node = TreeNode(nums[midIndex])
        node.left = self.sortedArrayToBST(nums[:midIndex])
        start = midIndex + 1
        if start < len(nums):
            node.right = self.sortedArrayToBST(nums[start:])
        return node
    
    def pathSum(self, root, sum):
        if not root:
            return []
        result = []
        def loop(node, current, stack):
            current = current + node.val
            stack.append(node.val)
            if node.left == None and node.right == None:
                if current == sum:
                    result.append(stack)
            if node.left != None:
                loop(node.left, current, stack[:])
            if node.right != None:
                loop(node.right, current, stack[:])
        loop(root, 0, [])
        return result
    
    ''' Flatten Binary Tree to Linked List'''
    def flatten(self, root):
        def flatten(self, root):
            def loop(node):
                temp = node.right
                last = node
                if node.left != None:
                    node.right = node.left
                    last = loop(node.right)
                    node.left = None
                if temp != None:
                    last.right = temp
                    last = loop(temp)
                return last
        if root != None:
            loop(root)

    '''Given a binary tree, determine if it is a valid binary search tree (BST).'''
    def isValidBST(self, root):
        def valid(node, minNum, maxNum):
            if node == None:
                return True
            if node.val >= maxNum or node.val <= minNum:
                return False
            return valid(node.left, minNum, node.val) and valid(node.right, node.val, maxNum)
        return valid(root, -sys.maxint-1, sys.maxint)
    
    '''Two elements of a binary search tree (BST) are swapped by mistake.'''
    def recoverTree(self, root):
        cur = root
        pre = None
        p1 = None
        p2 = None
        # TODO
    
    '''Given a binary tree, return all root-to-leaf paths.'''
    def binaryTreePaths(self, root):
        if root == None:
            return []
        result = []
        def loop(node, valueString):
            if valueString:
                valueString = valueString + "->" + str(node.val)
            else:
                valueString = str(node.val)
            if node.left == None and node.right == None:
                result.append(valueString)
            if node.left != None:
                loop(node.left, valueString)
            if node.right != None:
                loop(node.right, valueString)
        loop(root, "")
        return result

    '''Sum Root to Leaf Numbers'''
    def sumNumbers(self, root):
        if root == None:
            return []
        result = []
        def loop(node, valueString):
            valueString += str(node.val)
            if node.left == None and node.right == None:
                result.append(valueString)
            if node.left != None:
                loop(node.left, valueString)
            if node.right != None:
                loop(node.right, valueString)
        loop(root, "")
        result = map(lambda x: int(x), result)
        return sum(result)
    

            
                



            
            
        


                
                
                    
                


        

       

                
        
    
    
        


        

            

        



                
            
            
        
            

        
        
        
        
            



        
     
   
        
        
        
            


        
    