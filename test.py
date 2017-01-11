#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
import PyCode
import sys

class ArrayTestCase(unittest.TestCase):
    def setUp(self):
        self.code = PyCode.ArrayCode()

    def test_removeElement(self):
        funcName = sys._getframe().f_code.co_name
        print funcName
        array = [0,4,4,0,4,4,4,0,2]
        self.code.removeElement(array, 4) 
        assert array == [0,0,0,2], 'wrong ' + funcName

        array = [3,2,2,3]
        self.code.removeElement(array, 3) 
        assert array == [2,2], 'wrong ' + funcName

    def test_removeDuplicates(self):
        funcName = sys._getframe().f_code.co_name
        print funcName
        array = [0,1,2,3,3,3,4,4]
        self.code.removeDuplicates(array) 
        assert array == [0,1,2,3,4], 'wrong ' + funcName
    
    def test_plusOne(self):
        funcName = sys._getframe().f_code.co_name
        print funcName
        assert self.code.plusOne([0]) == [1], 'wrong ' + funcName
        assert self.code.plusOne([9]) == [1,0], 'wrong ' + funcName

    def test_pascalTriangle(self):
        funcName = sys._getframe().f_code.co_name
        print funcName
        assert self.code.pascalTriangle(1) == [[1]], 'wrong ' + funcName
        assert self.code.pascalTriangle(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]], 'wrong ' + funcName

    def test_getPascalTriangleRow(self):
        funcName = sys._getframe().f_code.co_name
        print funcName
        assert self.code.getPascalTriangleRow(1) == [1,1], 'wrong ' + funcName
        assert self.code.getPascalTriangleRow(4) == [1,4,6,4,1], 'wrong ' + funcName
        print self.code.getPascalTriangleRow(21)
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
        