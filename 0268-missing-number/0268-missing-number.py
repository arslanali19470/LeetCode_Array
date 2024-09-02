class Solution(object):
    def missingNumber(self, nums):
        # for num in range(len(nums)+1):
        #     if nums.count(num)==0:
        #         return num
        num=len(nums)
        TotalSum=num*(num+1)//2
        actual_sum=sum(nums)
        return TotalSum-actual_sum


        