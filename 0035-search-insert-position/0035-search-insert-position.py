class Solution(object):
    def searchInsert(self, nums, target):
        lowP,highP=0,len(nums)-1
        while lowP<=highP:
            midValue=(lowP+highP)//2
            if nums[midValue]==target:
                return midValue
            if nums[midValue]>target:
                highP=midValue-1
            else:
                lowP=midValue+1
        return lowP
            
       
            
