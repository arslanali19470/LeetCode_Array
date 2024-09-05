class Solution(object):
    def missingRolls(self, rolls, mean, n):
        m=len(rolls)
        TotalSum=(m+n)*mean
        mSum=sum(rolls)
        nSum=TotalSum-mSum
        if nSum>n*6 or nSum<n:
            return []

        result=[]
        result=[1]*n
        nSum=nSum-n

        for i in range(n):
            add=min(5,nSum)
            result[i]+=add
            nSum=nSum-add

        return result





        