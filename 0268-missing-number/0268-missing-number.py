class Solution(object):
    def missingNumber(self, nums):
        for num in range(len(nums)+1):
            if nums.count(num)==0:
                return num

        