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
        result = [1, 1]
        for j in range(2, rowIndex + 1):
            result.append(1)
            temp = 1
            for i in range(0, j + 1):
                if i == 0 or i == j:
                    result[i] = 1
                elif j - i < j / 2.0:
                    result[i] = result[j - i]
                else: 
                    newTemp = result[i]
                    result[i] = temp + result[i]
                    temp = newTemp               
        return result

    '''Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.'''
    def mergeArray(self, nums1, m, nums2, n):
        diff = len(nums1) - m
        while diff > 0:
            nums1.pop()
            diff -= 1
        i = 0
        for j in range(0, n):
            count = len(nums1)
            while (i < count):
                if nums1[i] >= nums2[j]:
                    nums1.insert(i, nums2[j])
                    break
                else:
                    i += 1
            if i == count:
                nums1.insert(i, nums2[j])
                i += 1
    
    '''Given an array of intergers, find two numbers such that they add up to a specific target number. 
    The function twoSum should return indices of the two numbers such that they add up to the target, 
    where index1 must be less than index2 Please note that your returned answers (both index1 and index2) are not zero-based.
    You may assume that each input would have exactly one solution.Input: numbers={2, 7, 11, 15}, target=9 Output: index1=1, index2=2'''
    def twoSum(self, nums, target):
        import collections
        counter = collections.Counter(nums)
        for index, value in enumerate(nums):
            anotherNum = target - value
            if (anotherNum != value and counter[anotherNum] != 0) or (anotherNum == value and counter[anotherNum] > 1):
                anotherIndex = nums[index + 1:len(nums)].index(anotherNum)
                return [index, index + 1 + anotherIndex] 

    '''Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
    Find all unique triplets in the array which gives the sum of zero.
    Note: Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c) 
    The solution set must not contain duplicate triplets.'''
    def threeSum(self, nums):
        newNums = sorted(nums)
        result = []
        for i in range(0, len(newNums) - 2):
            if i > 0 and newNums[i] == newNums[i - 1]:
                continue
            j = i + 1
            k = len(newNums) - 1
            while j < k:
                number = newNums[i] + newNums[j] + newNums[k]
                if number == 0:
                    temp = [newNums[i], newNums[j], newNums[k]]
                    result.append(temp)
                    while True:
                        k -= 1
                        if j >= k or newNums[k] != newNums[k+1]:
                            break
                    while True:
                        j += 1
                        if j >= k or newNums[j] != newNums[j-1]:
                            break
                elif number > 0:
                    while True:
                        k -= 1
                        if j >= k or newNums[k] != newNums[k+1]:
                            break
                else:
                    while True:
                        j += 1
                        if j >= k or newNums[j] != newNums[j-1]:
                            break
        return result

    '''Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
    Return the sum of the three integers. You may assume that each input would have exactly one solution.'''
    def threeSumClosest(self, nums, target):
        if len(nums) < 3:
            return 
        newNums = sorted(nums)
        result = nums[0] + nums[1] + nums[2]
        for i in range(0, len(newNums) - 2):
            if i > 0 and newNums[i] == newNums[i - 1]:
                continue
            j = i + 1
            k = len(newNums) - 1
            while j < k:
                number = newNums[i] + newNums[j] + newNums[k]
                if abs(number - target) < abs(result - target):
                    result = number
                elif number - target > 0:
                    while True:
                        k -= 1
                        if j >= k or newNums[k] != newNums[k+1]:
                            break
                else:
                    while True:
                        j += 1
                        if j >= k or newNums[j] != newNums[j-1]:
                            break
        return result

        '''Given an array S of n integers, are there elements a, b, c and d in S such that a+b+c+d = target? 
        Find all unique quadruplets in the array which gives the sume of target.
        Note:Elements in quadruplets (a, b, c, d) must be in non-descending order. (ie, a<=b<=c<=d)
        The solution must not contain duplicates quadruplets.'''
    def fourSum(self, nums, target):
        newNums = sorted(nums)
        result = []
        h = 0
        while h < len(newNums) - 3:
            smallTarge = target - newNums[h]      
            tempResult = []
            i = h + 1
            while i < len(newNums) - 2:    
                j = i + 1
                k = len(newNums) - 1
                while j < k:
                    number = newNums[i] + newNums[j] + newNums[k]
                    if number == smallTarge:
                        temp = [newNums[i], newNums[j], newNums[k]]
                        tempResult.append(temp)
                        while True:
                            k -= 1
                            if j >= k or newNums[k] != newNums[k+1]:
                                break
                        while True:
                            j += 1
                            if j >= k or newNums[j] != newNums[j-1]:
                                break
                    elif number > smallTarge:
                        while True:
                            k -= 1
                            if j >= k or newNums[k] != newNums[k+1]:
                                break
                    else:
                        while True:
                            j += 1
                            if j >= k or newNums[j] != newNums[j-1]:
                                break
                while True:
                    i += 1
                    if i >= len(newNums) - 2 or newNums[i] != newNums[i - 1]:
                        break
            if len(tempResult) > 0:
                for value in tempResult:
                    value.insert(0, newNums[h])
                    result.append(value) 
            while True:
                    h += 1
                    if h >= len(newNums) - 3 or newNums[h] != newNums[h - 1]:
                        break                  
        return result

    '''Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
    To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. 
    All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.'''
    def fourSumCount(self, A, B, C, D):
        pass
        
    '''Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
    Find the minimum element.
    You may assume no duplicate exists in the array.'''
    def findMin(self, nums):
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return nums[0] if nums[0] < nums[1] else nums[1]
        if nums[0] < nums[-1]:
            return nums[0]
        mid = len(nums) / 2
        if nums[mid] > nums[0]:
            return self.findMin(nums[mid:])
        else :
            return self.findMin(nums[:mid+1])
    
    '''Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
    Find the minimum element.
    The array may contain duplicates.'''
    def findMin2(self, nums):
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return nums[0] if nums[0] < nums[1] else nums[1]
        start = 0
        end = len(nums) - 1
        while True:
            if start >= end:
                return nums[start]
            elif nums[start] != nums[end]:
                break
            start += 1
        if nums[start] < nums[end]:
            return nums[start]
        mid = start + (len(nums) - start)/ 2
        if nums[mid] >= nums[start]:
            return self.findMin2(nums[mid:])        
        else :
            return self.findMin2(nums[start:mid+1])
        
    '''Largest Rectangle in Histogram
    https://leetcode.com/problems/largest-rectangle-in-histogram/'''
    def largestRectangleArea(self, heights):
        s = []
        heights = heights[:]
        heights.append(0);
        sum = 0
        i = 0
        while i < len(heights):
            if len(s) == 0 or heights[i] > heights[s[-1]]:
                s.append(i)
                i += 1
            else:
                t = s[-1]
                del s[-1]
                sum = max(sum, heights[t] * (i if len(s) == 0 else i - s[-1] - 1))
        return sum

    '''Given a 2D binary matrix filled with 0's and 1's, 
    find the largest rectangle containing all ones and return its area.'''
    def maximalRectangle(self, matrix):
        if len(matrix) == 0:
            return 0
        result = 0
        nums = map(lambda x:int(x) ,list(matrix[0]))
        for i in range(0, len(matrix)):
            if i != 0:
                for idx in range(0, len(nums)):
                    string = matrix[i]
                    val = int(string[idx])
                    nums[idx] = val if val == 0 else nums[idx] + val
            tempMax = self.largestRectangleArea(nums)
            result = max(result, tempMax)
        return result
    
    '''Determine whether an integer is a palindrome. Do this without extra space.'''
    def isPalindrome(self, x):
        if x < 0:
            return False
        string = str(x)
        for i in range(0, len(string) / 2):
            if string[i] != string[-(i+1)]:
                return False
        return True
    
    '''Write an efficient algorithm that searches for a value in an m x n matrix. 
    This matrix has the following properties:
    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.'''
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        array = map(lambda x:x[0], matrix)
        start = 0
        end = m - 1
        while end - start > 1:
            mid = (start + end) / 2
            if target > array[mid]:
                start = mid
            elif target < array[mid]:
                end = mid
            else:
                return True
        if target < array[end]:
            i = start
        elif target == array[end]:
            return True
        elif target > matrix[m-1][n-1]:
            return False
        else:
            i = end
        from bisect import bisect_left    
        index = bisect_left(matrix[i], target) 
        if index < len(matrix[i]) and matrix[i][index] == target:
            return True
        else:
            return False
    
    '''Write an efficient algorithm that searches for a value in an m x n matrix. 
    This matrix has the following properties:
    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.'''
    def searchMatrix2(self, matrix, target):
       
        row = len(matrix)
        if row == 0:
            return False
        col = len(matrix[0])
        if col == 0:
            return False
        i = col - 1
        j = 0
        while j < row and i >= 0:
            value = matrix[j][i]
            if target > value:
                j += 1
            elif target < value:
                i -= 1
            else: 
                return True
        return False   
       

            
                
            
        
            
            

        
                        
                    
                
        
        
        
    

        

            
        
           


                
        
       
        
            


            
        


             

