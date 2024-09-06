class Solution(object):
    def maxArea(self, height):
        lenarray=len(height)
        firstP=0
        maxarea=0
        secondP=lenarray-1
        while(firstP<secondP):
            diff=secondP-firstP
            area = diff * min(height[firstP], height[secondP])
            maxarea = max(maxarea, area)
            if height[firstP]<height[secondP]:
                firstP+=1
            else:
                secondP-=1
        return maxarea






        