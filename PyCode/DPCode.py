import sys


class DPCode:
    def __init__(self):
        pass

    class TreeNode(object):
         def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

    '''Best Time to Buy and Sell Stock'''
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        profit = max(0, prices[1] - prices[0])
        minValue = min(prices[1], prices[0])
        for i in range(2,len(prices)):
            cuValue = prices[i]
            if cuValue > minValue:
                profit = max(profit, cuValue - minValue)
            else:
                minValue = cuValue
        return profit
    
    '''Best Time to Buy and Sell Stock II'''
    def maxProfit2(self, prices):
        if len(prices) <= 1:
            return 0
        profit = 0
        for i in range(1,len(prices)):
            last = prices[i-1]
            current = prices[i]
            if current > last: 
                profit += current - last
        return profit
    
    '''Best Time to Buy and Sell Stock III'''
    def maxProfit3(self, prices):
        profit = [0] * len(prices)
        if len(prices) < 2:
            return 0
        minNum = prices[0]
        for i in range(1, len(prices)):
            minNum = min(minNum, prices[i])
            if i == 1:
                profit[i] = prices[1] - prices[0] if prices[1] > prices[0] else 0
            else:
                profit[i] =  max(profit[i-1], prices[i] - minNum)
        result = 0
        maxNum = prices[-1]
        lastProfit = 0
        for i in range(len(prices) - 2, -1, -1):
            maxNum = max(maxNum, prices[i])
            if i == len(prices) - 2:
                profit[i] += prices[len(prices) - 1] - prices[len(prices) - 2] if prices[len(prices) - 1] > prices[len(prices) - 2] else 0
            else:
                lastProfit =  max(lastProfit, maxNum - prices[i])

            result = max(profit[i] + lastProfit, result)
        return result
    
    '''Unique Paths'''
    def uniquePaths(self, m, n):
        array = [[0 for col in range(n)] for row in range(m)]  
        for i in range(0, m):
            for j in range(0, n):
                if i == 0 or j == 0:
                    array[i][j] = 1
                    continue
                array[i][j] = array[i-1][j] + array[i][j-1]
        return array[m-1][n-1]
    
    '''Unique Paths II'''
    """
        :type obstacleGrid: List[List[int]]
        :rtype: int
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        array = [[0 for col in range(n)] for row in range(m)] 
        for i in range(0, m):
            for j in range(0, n):
                if i == 0 and j == 0:
                    if obstacleGrid[i][j] != 1:
                        array[0][0] = 1
                    continue
                if i > 0 and obstacleGrid[i][j] != 1:
                    array[i][j] += array[i-1][j]
                if j > 0 and obstacleGrid[i][j] != 1:
                    array[i][j] += array[i][j-1]
        return array[m-1][n-1]
    
    '''Minimum Path Sum'''
    def minPathSum(self, grid):
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        array = [[0 for col in range(n)] for row in range(m)]
        for i in range(0, m):
            for j in range(0, n):
                if i == 0 and j == 0:
                    array[i][j] = grid[i][j]
                elif i == 0:
                    array[i][j] = array[i][j-1] + grid[i][j]
                elif j == 0:
                    array[i][j] = array[i-1][j] + grid[i][j]
                else:
                    array[i][j] = min(array[i-1][j], array[i][j-1]) + grid[i][j]
        return array[m-1][n-1]
    
    '''Maximum Subarray'''
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return 0
        dp = [0] * len(nums)
        dp[0] = nums[0]
        maxNum = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            maxNum = max(dp[i], maxNum)
        return maxNum
    
    '''Maximum Product Subarray'''
    def maxProduct(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        minP = nums[0]
        maxP = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            temp = maxP
            maxP = max(maxP * nums[i], minP * nums[i], nums[i]) 
            minP = min(temp * nums[i], minP * nums[i], nums[i])
            result = max(maxP, result)
        return result
    
    '''Climbing Stairs'''
    def climbStairs(self, n):
        if n <= 1:
            return 1
        if n == 2:
            return 2
        array = [0] * n
        array[0] = 1
        array[1] = 2
        for i in range(2, n):
            array[i] = array[i-1] + array[i-2]
        return array[n-1]
    
    '''Triangle'''
    '''Given a triangle, find the minimum path sum from top to bottom. 
    Each step you may move to adjacent numbers on the row below.'''
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """  
        m = len(triangle)
        if m == 0:
            return 0
        if m == 1:
            return triangle[0][0]
        array = [0] * m
        array[0] = triangle[0][0]
        for i in range(1, m):
            for j in range(len(triangle[i])-1, -1, -1):
                if j == 0:
                    array[0] = array[0] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    array[j] = array[j-1] + triangle[i][j]
                else:
                    array[j] = min(array[j], array[j-1]) + triangle[i][j]
        return min(array)
    
    '''Unique Binary Search Trees'''
    def numTrees(self, n):
        if n <= 1:
            return n
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        for i in range(2, n+1):
            for j in range(0,i):
                dp[i] += dp[j] * dp[i-j-1]
        return dp[n]

    '''Unique Binary Search Trees II'''
    def generateTrees(self, n): 
        if n <= 0:
            return []
        def loop(start, stop):
            result = []
            if start > stop:
                result.append(None)
                return result
            for i in range(start, stop+1):
                left = loop(start, i-1)
                right = loop(i+1, stop)
                for j in range(0, len(left)):
                    for k in range(0, len(right)):
                        node = TreeNode(i)
                        node.left = left[j]
                        node.right = right[k]
                        result.append(node)
            return result
        return loop(1, n)
    
    '''Perfect Squares'''
    def numSquares(self, n):
        dp = [sys.maxint] * (n + 1)
        dp[0] = 0
        for i in range(0, n+1):
            j = 1
            while i+j*j <= n:
                index = i+j*j
                dp[index] = min(dp[i]+1, dp[index])
                j+=1
        return dp[n]
    
    
            

        
                

            

            
                


                    
        
       
        

        

            
            
        
        
        
                
                
            


    

