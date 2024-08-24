class Solution(object):
    def twoSum(self, nums, target):
        MainObject={}
        for i,n in enumerate(nums):
            diffNum=target-n
            if diffNum in MainObject:
                return [MainObject[diffNum], i]
            MainObject[n]=i
 
        