class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        MainObj={}
        for i,n in enumerate(nums):
            if n in MainObj and abs(i-MainObj[n])<=k:
                return True
            MainObj[n]=i
        return False

   
                





        