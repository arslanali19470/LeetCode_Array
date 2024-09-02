class Solution(object):
    def majorityElement(self, nums):
        MainObj = {}
        for num in nums:
            if num in MainObj:
                MainObj[num]+=1
            else:
                MainObj[num]=1
            
            if MainObj[num]>len(nums)/2:
                return num
        

