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


            
                
