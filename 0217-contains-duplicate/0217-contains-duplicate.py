class Solution(object):
    def containsDuplicate(self, nums):
        Mainobj={}
        for num in nums:
            if num in Mainobj:
                return True
            Mainobj[num]=1
        return False
       
      


      
           

        