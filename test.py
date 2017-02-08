#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
import PyCode
import sys

class ArrayTestCase(unittest.TestCase):
    def setUp(self):
        self.code = PyCode.ArrayCode()

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

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
        