class Solution(object):
    def moveZeroes(self, nums):
        start=0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[start]=nums[start], nums[i]
                start+=1
        return nums
  
        
 


        