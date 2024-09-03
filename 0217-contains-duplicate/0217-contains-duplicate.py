class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        for num in range(1,len(nums)):
            if nums[num] == nums[num-1]:
                return True
        return False 
      


      
           

        