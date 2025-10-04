class Solution:
    def maxArea(self, height: List[int]) -> int:
        m1=0
        m2=len(height)-1
        ma=0

        while m1<m2:
            h=min(height[m1],height[m2])
            w=m2-m1
            a=h*w
            ma=max(ma,a)

            if height[m1]<height[m2]:
                m1+=1
            else:
                m2-=1

        return ma
