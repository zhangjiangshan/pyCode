
class BackTrackingCode:
    
    def __init__(self):
        pass
    
    '''Given two integers n and k, 
    return all possible combinations of k numbers out of 1 ... n.'''
    def combine(self, n, k):
        if n == k or k == 0:
            row = []
            for i in range(1, k+1):
                row.append(i)
            return [row]
                
        array1 = self.combine(n-1, k-1)
        array2 = self.combine(n-1, k)
        for obj in array1:
            obj.append(n)
        result = array1 + array2
        return result
    
    '''Combination Sum'''
    def combinationSum(self, candidates, target):
        pass
       # TODO
    
    '''Subsets'''
    def subsets(self, nums):
        result = [[]]
        if len(nums) == 0:
            return result
        stack = []
        def loop(start, temp):
            if len(nums) == start:
                return 
            i = start
            while i >= start and i < len(nums):
                temp.append(nums[i])
                result.append(temp[:])
                loop(i+1, temp[:])
                temp.pop()
                #while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                    #i += 1
                i += 1
        loop(0, [])
        return result
    
    '''Permutations'''
    def permute(self, nums):
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        result = []
        def loop(n, stack):
            if len(n) == 2:
                result.append(stack + n[:])
                result.append(stack + [n[1], n[0]])
                return
            for i in range(0, len(n)):
                cur = n[i]
                stack.append(cur)
                array = n[:]
                array.pop(i)
                loop(array, stack)
                stack.pop()
        loop(nums,[])
        return result
    
    '''search words II'''
    def wordSearchII(self, board, words):
        class Node:
            def __init__(self):
                self.dict = {}
                self.word = None
        root = Node() 
        p = root
        for word in words:
            p = root
            for c in word:
                if c not in p.dict:
                    p.dict[c] = Node()
                p = p.dict[c]
            p.word = word
            
        res = []
        def find(p, i, j):
            c = board[i][j]
            if p.word != None:
                res.append(p.word)
                p.word = None
            if c not in p.dict or c == '#':
                return
            temp = p.dict[c]
            board[i][j] = '#'
            if i - 1 >= 0:
                find(temp, i-1, j)
            if j - 1 >= 0:
                find(temp, i, j-1)
            if i + 1 < len(board):
                find(temp, i+1, j)
            if j + 1 < len(board[i]):
                find(temp, i, j+1)
            board[i][j] = c
        
        for i,a in enumerate(board):
            for j,b in enumerate(a):
                find(root, i, j)
        return res


        while low <= high:
            mid = (low + high) / 2
            if target < mid:
                hight = mid -1 
            else:
                low = mid + 1
