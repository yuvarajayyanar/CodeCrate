class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m=s=nums[0]
        
        for i in range(1,len(nums)):
            s=max(nums[i],nums[i]+s)
            m=max(s,m)
        return m
