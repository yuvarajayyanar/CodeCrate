class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        
        while l<=r:
            mid=(l+r)//2
            m=0
            if nums[mid]>nums[mid+1] or nums[mid]==nums[mid+1]:
                m=mid
                r=mid-1
            else:
                l=mid+1
                if m<l:
                    m=l
        return m
                

