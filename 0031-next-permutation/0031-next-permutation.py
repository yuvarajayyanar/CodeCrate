class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)

        p1=n-2

        while p1>=0 and nums[p1]>=nums[p1+1]:
            p1-=1
        if p1>=0:
            p2=n-1
            while nums[p2]<=nums[p1]:
                p2-=1
            nums[p1],nums[p2]=nums[p2],nums[p1]

        l,r=p1+1,n-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
        return nums