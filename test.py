#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
import PyCode
import sys

class ArrayTestCase(unittest.TestCase):
    def setUp(self):
        self.code = PyCode.ArrayCode()
        self.bit = PyCode.BitCode()
        self.tree = PyCode.TreeCode()
        self.dp = PyCode.DPCode()
        self.bt = PyCode.BackTrackingCode()
        self.other = PyCode.OtherCode()
        self.linkedList = PyCode.LinkedListCode()




    def use_log(func):
        def wrapper(*args):
            print func.__name__
            return func(*args)
        return wrapper
        
    @use_log
    def test_removeElement(self):
        array = [0,4,4,0,4,4,4,0,2]
        self.code.removeElement(array, 4) 
        assert array == [0,0,0,2], 'wrong ' + funcName
        array = [3,2,2,3]
        self.code.removeElement(array, 3) 
        assert array == [2,2], 'wrong ' + funcName

    @use_log
    def test_removeDuplicates(self):
        array = [0,1,2,3,3,3,4,4]
        self.code.removeDuplicates(array) 
        assert array == [0,1,2,3,4], 'wrong ' + funcName

    @use_log
    def test_plusOne(self):
        assert self.code.plusOne([0]) == [1], 'wrong ' + funcName
        assert self.code.plusOne([9]) == [1,0], 'wrong ' + funcName

    @use_log
    def test_pascalTriangle(self):
        assert self.code.pascalTriangle(1) == [[1]], 'wrong ' + funcName
        assert self.code.pascalTriangle(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]], 'wrong ' + funcName

    @use_log
    def test_getPascalTriangleRow(self):
        assert self.code.getPascalTriangleRow(2) == [1,2,1], 'wrong ' + funcName
        assert self.code.getPascalTriangleRow(1) == [1,1], 'wrong ' + funcName
        assert self.code.getPascalTriangleRow(4) == [1,4,6,4,1], 'wrong ' + funcName

    @use_log
    def test_mergeArray(self):
        nums = [1,2,3,0,0,0]
        self.code.mergeArray(nums, 3, [2,5,6],3)
        assert nums == [1,2,2,3,5,6], 'wrong ' + funcName

    @use_log
    def test_twoSum(self):
        assert self.code.twoSum([3,2,4], 6) == [1,2], 'wrong ' + funcName

    @use_log
    def test_threeSum(self):
        result = self.code.threeSum([-1, 0, 1, 2, -1, -4]) 
        assert len(result) == 2 and [-1, 0, 1] in result and [-1, -1, 2] in result, 'wrong ' + funcName 

    @use_log
    def test_threeSumClosest(self):
        result = self.code.threeSumClosest([1,2,4,8,16,32,64,128], 82) 
        assert result == 82, 'wrong ' + funcName

    @use_log
    def test_fourSum(self):
        assert self.code.fourSum([0,0,0,0], 0) == [[0,0,0,0]], 'wrong ' + funcName
        assert self.code.fourSum([1,0,-1,0,-2,2], 0) == [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]], 'wrong ' + funcName
    
    @use_log
    def test_findMin(self):
        assert self.code.findMin([3,1,2]) == 1, 'wrong ' + funcName
        assert self.code.findMin([4,5,6,7,0,1,2]) == 0, 'wrong ' + funcName
    
    @use_log
    def test_findMin2(self):
        assert self.code.findMin2([1,1,3,1]) == 1, 'wrong ' + funcName
    
    @use_log
    def test_largestRectangleArea(self):
        assert self.code.largestRectangleArea([3,6,5,7,4,8,1]) == 20, 'wrong ' + funcName
        assert self.code.largestRectangleArea([2,1,5,6,2,3]) == 10, 'wrong ' + funcName
        assert self.code.largestRectangleArea([0,0,0,0,0,0,0,0,2147483647]) == 2147483647, 'wrong ' + funcName

    @use_log
    def test_maximalRectangle(self):
        assert self.code.maximalRectangle(["01","10"]) == 1, 'wrong ' + funcName
        assert self.code.maximalRectangle(["0000","1111","1110","0100"]) == 6, 'wrong ' + funcName
    
    @use_log
    def test_isPalindrome(self):
        assert self.code.isPalindrome(121) == True, 'wrong ' + funcName
    
    @use_log
    def test_searchMatrix(self):
        assert self.code.searchMatrix([[1],[3]], 3) == True, 'wrong ' + funcName
        assert self.code.searchMatrix([[1,3,5]], 0) == False, 'wrong ' + funcName
        assert self.code.searchMatrix([[1],[3]], 2) == False, 'wrong ' + funcName
        assert self.code.searchMatrix([[1]], 0) == False, 'wrong ' + funcName

    @use_log
    def test_searchMatrix2(self):
        assert self.code.searchMatrix2([[1,4],[2,5]],2) == True, 'wrong ' + funcName 
        assert self.code.searchMatrix2([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]], 15) == True, 'wrong ' + funcName 
        assert self.code.searchMatrix2([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5) == True, 'wrong ' + funcName  
    
    @use_log
    def test_searchRange(self):
        assert self.code.searchRange([5, 7, 7, 8, 8, 10], 8) == [3,4], 'wrong ' + funcName 

    @use_log
    def test_searchInsert(self):
        assert self.code.searchInsert([1,3,5], 4) == 2, 'wrong ' + funcName 
        assert self.code.searchInsert([1,3], 2) == 1, 'wrong ' + funcName 
        assert self.code.searchInsert([1], 2) == 1, 'wrong ' + funcName 

    @use_log
    def test_isValidBST(self):
        node = PyCode.TreeCode.TreeNode(2)
        node.left = PyCode.TreeCode.TreeNode(1)
        node.right = PyCode.TreeCode.TreeNode(3)
        assert self.tree.isValidBST(node) == True, 'wrong ' + funcName 
    
    @use_log
    def test_maxProfit(self):
        assert self.dp.maxProfit([7,1,5]) == 4, 'wrong' 
    
    @use_log
    def test_uniquePaths(self):
         assert self.dp.uniquePaths(2, 2) == 2, 'wrong' 
    
    @use_log
    def test_uniquePathsWithObstacles(self):
        assert self.dp.uniquePathsWithObstacles([[0,1],[0,0]]) == 1, 'wrong'

        assert self.dp.uniquePathsWithObstacles([[0],[0]]) == 1, 'wrong'
        assert self.dp.uniquePathsWithObstacles([[0,0]]) == 1, 'wrong'

        
        assert self.dp.uniquePathsWithObstacles([[0,1]]) == 0, 'wrong'
    
    @use_log
    def test_minimumTotal(self):
        assert self.dp.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]) == 11, 'wrong'
        assert self.dp.minimumTotal([[1],[2,3]]) == 3, 'wrong'
    
    @use_log
    def test_generateTrees(self):  
        assert self.dp.generateTrees(0) == [], 'wrong'
    
    @use_log
    def test_numSquares(self):  
        assert self.dp.numSquares(12) == 3, 'wrong'
    
    @use_log
    def test_subsets(self):
        assert self.bt.subsets([1,2,3]) == [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]], 'wrong'
        
    @use_log
    def test_permute(self):
        assert self.bt.permute([1,2,3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]], 'wrong'
    
    @use_log
    def test_reverse(self):
        assert self.other.reverse(-123) == -321, 'wrong'
        assert self.other.reverse(123) == 321, 'wrong'
    
    @use_log
    def test_calculate(self):
        assert self.other.calculate("14-3/2") == 13, 'wrong'
        assert self.other.calculate("  30") == 30, 'wrong'
        assert self.other.calculate("4  ") == 4, 'wrong'
        assert self.other.calculate("1+2*3") == 7, 'wrong'
        assert self.other.calculate("0/1") == 0, 'wrong'

    @use_log 
    def test_deleteDuplicates2(self):
        node = PyCode.LinkedListCode.ListNode(1)
        node.next = PyCode.LinkedListCode.ListNode(2)
        node.next.next = PyCode.LinkedListCode.ListNode(2)
        assert self.linkedList.deleteDuplicates2(node) == node, 'wrong'
    
    @use_log
    def test_partition(self):
         node = PyCode.LinkedListCode.ListNode(1)
         node.next = PyCode.LinkedListCode.ListNode(2)
    
    @use_log
    def test_copyRandomList(self):
        node = PyCode.LinkedListCode.RandomListNode(-1)
        node.next = PyCode.LinkedListCode.RandomListNode(-1)
        self.linkedList.copyRandomList(node)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
        