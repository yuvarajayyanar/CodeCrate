class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ws=sum(nums[0:k])
        ms=ws
        n=len(nums)
        for i in range(k,n):
            ws=ws+nums[i]-nums[i-k]
            ms=max(ws,ms)

        return (ms/k)
