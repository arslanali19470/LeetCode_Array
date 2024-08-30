class Solution(object):
    def plusOne(self, digits):
        for n in reversed(range(len(digits))):
            if digits[n] != 9:
                digits[n]+=1
                return digits
            digits[n]=0
        return [1]+digits


            
            


        