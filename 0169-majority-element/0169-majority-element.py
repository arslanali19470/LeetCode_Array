class Solution(object):
    def majorityElement(self, nums):
        MainObj = {}
        
        for num in nums:  # Use the element instead of the index
            if num in MainObj:
                MainObj[num] += 1
            else:
                MainObj[num] = 1
                
            # Early return if the majority element is found
            if MainObj[num] > len(nums) // 2:
                return num
