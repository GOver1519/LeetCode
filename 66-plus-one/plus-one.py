class Solution(object):
    def plusOne(self, digits):
        i = 0
        sum = 0
        while i<len(digits):
            sum = sum * 10 + digits[i]
            i = i+1
        sum+=1
        a=str(sum)
        result = []  
        for i in range(len(a)):
            result.append(sum % 10)   
            sum //= 10

        result.reverse() 
        return result
        