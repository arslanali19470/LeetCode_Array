class Solution(object):
    def moveZeroes(self, nums):
        for ind,num in enumerate(nums):
            if num ==0:
                nums.remove(num)
                nums.append(0)
        return nums
        
 


        