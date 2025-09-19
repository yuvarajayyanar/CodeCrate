class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        n=len(nums)
        avgs=[-1]*n

        windowsize=2*k+1
        if windowsize>n:
            return avgs

        prefix_sum=[0]*(n+1)
        for i in range(n):
            prefix_sum[i+1]=prefix_sum[i]+nums[i]

        for i in range(k,n-k):
            total=prefix_sum[i+k+1]-prefix_sum[i-k]
            avg=total//windowsize
            avgs[i]=avg

        
        
        return avgs