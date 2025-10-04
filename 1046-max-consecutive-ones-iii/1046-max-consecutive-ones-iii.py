class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        n=len(nums)
        k1=0
        ans=0


        for right in range(n):
            if nums[right]==0:
                k1+=1

            while k1>k:
                if nums[l]==0:
                    k1-=1
                l+=1
            ans=max(ans,right-l+1)
        return ans
