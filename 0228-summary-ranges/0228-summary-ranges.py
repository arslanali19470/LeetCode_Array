class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []
        array=[]
        start,end=nums[0],nums[0]
        for i in range(1,len(nums)):
            if nums[i] > end+1:
                if start != end:
                    array.append(str(start) +"->"+ str(end))
                else:
                    array.append(str(end))
                start, end=nums[i],nums[i]
            else:
                end=nums[i]
             
        if start != end:
            array.append(str(start)+"->"+str(end))
        else:
            array.append(str(end))
        return array

                
                





        