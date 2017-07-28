from math import floor

class OtherCode:
    def __init__(self):
        pass
    
    ''' Reverse Integer'''
    def reverse(self, x):
        result = 0
        factor = 1 if x >= 0 else -1
        x *= factor
        while x:
            result = result * 10 + x % 10
            x /= 10
        result *= factor
        maxint = pow(2,31) - 1
        return result if -maxint-1 < result < maxint else 0
    
    '''Add Binary'''
    def addBinary(self, a, b):
        numa = 0
        for i in a:
            numa = numa * 2 + int(i)
        numb = 0
        for i in b:
            numb = numb * 2 + int(i)
        return "{0:b}".format(numa+numb)
    
    '''Basic Calculator II'''
    def calculate(self, s):
        stack = []
        last = 0
        operator = "+"
        for idx, val in enumerate(s):
            if val.isdigit():
                last = last* 10 + int(val)
            if idx == len(s)-1 or (not val.isdigit() and val != ' '):  
                if operator == "-":
                    stack.append(-last)
                elif operator == "+":
                    stack.append(last)
                elif operator == "*":
                    stack.append(stack.pop()*last)
                elif operator == "/":
                    temp = stack.pop()
                    if temp * last > 0:
                        temp = temp / last
                    else:
                        temp = -(-temp / last)
                    stack.append(temp)
                last = 0
                operator = val
        return sum(stack)
    
    '''Round numbers'''
    def roundNumbers(self, nums):
        result = map(lambda x: floor(x) ,nums)
        remain = round(sum(result) - sum(nums))
        it = sorted(enumerate(nums), key=lambda x: x[1] - floor(x[1]))
        for _ in range(remain):
            result[it.pop()[0]] += 1

    '''Merge Intervals'''
    class Interval(object):
        def __init__(self, s=0, e=0):
            self.start = s
            self.end = e

    def merge(self, intervals):
        result = []
        temp = sorted(intervals, key=lambda x:x.start)
        for i in temp:
            if result and i.start <= result[-1].end:
                result[-1].end = max(result[-1].end, i.end)
            else:
                result.append(i)
        return result
    
    '''Free Time
    A = [(1,2), (5,6)]
    B = [(1,3)]
    C = [(4,10)]
    Return the list of free intervals from all three, in this case would be: [(3,4)]'''

    def GetFreeTime(self, users):
        input =  [val for sublist in users for val in sublist]
        merge = self.merge(users)
        result = []
        lastEnd = 0
        for i in merge:
            if i.start == 0:
                lastEnd = i.end
                continue
            interval = Interval()
            interval.start = lastEnd
            interval.end = i.start
            result.append(interval)
        if not result:
            return result
        last = result[-1]
        if last.end != 23:
            interval = Interval()
            interval.start = last.end
            interval.end = 23
            result.append(interval)
        return result
    
    '''Insert Interval'''
    def insert(self, intervals, newInterval):
        l,r = [], []
        temp = Interval(newInterval.start, newInterval.end)
        for i in intervals:
            if i.end < newInterval.start:
                l.append(i)
            elif i.start > newInterval.end:
                r.append(i)
            else:
                temp.start = min(temp.start, i.start)
                temp.end = max(temp.end, i.end)
        return l + [temp] + r

            
            

                
                
                
                
            
        




            
                
