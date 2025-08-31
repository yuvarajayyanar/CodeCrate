class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return
        x=1
        n=len(nums)

        for i in range(x,n):
            if nums[i]!=nums[i-1]:
                nums[x]=nums[i]
                x+=1
        return x