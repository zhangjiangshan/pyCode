class GreedyCode:
    
    def __init__(self):
        pass

    def canJump(self, nums):
        if len(nums) == 0:
            return True
        v = nums[0]
        for i in range(1, len(nums)):
            v -= 1
            if v < 0:
                return False
            if v < nums[i]:
                v = nums[i]
        return True
    
    def canJump2(self, nums):
        step = cur = next = 0
        i = 0
        
        while i < len(nums):
            if cur >= len(nums) - 1:
                break
            while i <= cur:
                next = max(next, nums[i]+i)
                i += 1
            step += 1
            cur = next
        return step
    
    '''Gas Station'''
    def canCompleteCircuit(self, gas, cost):
        sum = 0
        k = 0
        total = 0
        for i in range(0, len(gas)):
            diff = gas[i] - cost[i]
            sum += diff
            total += diff
            if sum < 0:
                sum = 0
                k = i + 1
        if total < 0:
            return -1
        else:
            return k
        
        '''Candy'''
        def candy(self, ratings):
            candys = [1] * len(ratings)
            for i in range(1, len(ratings)):
                if ratings[i] > ratings[i-1]:
                    candys[i] = candys[i-1] + 1

            for i in range(len(ratings)-2, 0, -1):
                if ratings[i] > ratings[i+1] and candys[i] <= candys[i + 1]:
                    candys[i] = candys[i+1] + 1
            return sum(candys)   

        '''Word Break'''   
        def wordBreak(self, s, wordDict):
            pass
            
            
       
            
            
        