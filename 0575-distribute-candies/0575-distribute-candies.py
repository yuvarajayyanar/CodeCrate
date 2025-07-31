class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n= len(candyType)//2
        j=0
        d={}

        for i in range(len(candyType)):
            if candyType[i] not in d:
                d[candyType[i]]=1
                j+=1
            if j==n:
                break
        return j