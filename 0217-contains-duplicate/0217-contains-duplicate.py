class Solution(object):
    def containsDuplicate(self, nums):
        Mainset=set()
        for num in nums:
            if num in Mainset:
                return True
            Mainset.add(num)
        return False
       
      


      
           

        