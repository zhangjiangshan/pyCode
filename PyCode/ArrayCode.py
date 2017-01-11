#!/usr/bin/python
# -*- coding: UTF-8 -*-

class ArrayCode:
    def __init__(self):
        pass
        
    '''Given an array and a value, remove all instances of that > value in place and return the new length.
    The order of elements can be changed. It doesn't matter what you leave beyond the new length.'''
    def removeElement(self, nums, val):
        deleteCount = 0
        for i in range(0, len(nums)) :
            obj = nums[i - deleteCount]
            if obj == val : 
                del nums[i - deleteCount]
                deleteCount += 1
        return len(nums)

    '''Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
    Do not allocate extra space for another array, you must do this in place with constant memory.'''
    def removeDuplicates(self, nums):
        lastValue = None
        deleteCount = 0
        for i in range(0, len(nums)) :
            obj = nums[i - deleteCount]
            if obj == lastValue : 
                del nums[i - deleteCount]
                deleteCount += 1
            lastValue = obj
        return len(nums)

    '''Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
    You may assume the integer do not contain any leading zero, except the number 0 itself.
    The digits are stored such that the most significant digit is at the head of the list.'''
    def plusOne(self, digits):
        carry = 1
        for idx in range(len(digits) - 1, -1, -1):
            value = digits[idx]
            newValue = value + carry
            if newValue == 10:
                digits[idx] = 0
                if idx == 0:
                    digits.insert(0, 1)
            else:
                digits[idx] = newValue
                return digits
        return digits
    
    '''Given numRows, generate the first numRows of Pascal's triangle.
    For example, given numRows = 5, Return 
    [
     [1],
     [1,1],
     [1,2,1],
     [1,3,3,1],
     [1,4,6,4,1]
    ]'''
    def pascalTriangle(self, numRows):
        result = []
        for i in range(0, numRows):
            if i == 0:
                result.append([1])
                continue
            elif i == 1:
                result.append([1,1])
                continue
            temp = []
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    temp.append(result[i-1][j-1] + result[i-1][j])
            result.append(temp)
        return result

    '''Given an index k, return the kth row of the Pascal's triangle.
    For example, given k = 3,Return [1,3,3,1].'''
    def getPascalTriangleRow(self, rowIndex):
        if rowIndex < 0:
            return []
        elif rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        result = []
        f = lambda i,j: 1 if i == 0 or i == j else f(i-1, j-1) + f(i, j-1)
        for i in range(0, rowIndex + 1):
            if i == 0 or i == rowIndex:
                result.append(1)
            else: 
                result.append(f(i, rowIndex))
        return result
            


            
        


             

