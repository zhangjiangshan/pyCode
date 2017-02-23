class BitCode:
    def __init__(self):
        pass

    '''Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
    find the one that is missing from the array.
    For example,Given nums = [0, 1, 3] return 2.'''
    def missingNumber(self, nums):
        x = 0
        for i in range(len(nums)+1):
            x ^= i
        for i in nums:
            x ^= i
        return x

    '''Given an integer, write a function to determine if it is a power of two.'''
    def isPowerOfTwo(self, n):
        if n < 0:
            return False
        hasOne = False
        while n > 0:
            if n & 1 != 0:
                if hasOne == True:
                    return False
                else:
                    hasOne = True
            n >>= 1
        return hasOne

    '''Write a function that takes an unsigned integer and returns the number of "1" bits it has'''
    def hammingWeight(self, n):
        count = 0
        while n > 0:
            if n & 1 != 0 :
                count += 1
            n >>= 1
        return count
