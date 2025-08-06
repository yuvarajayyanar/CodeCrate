class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        x=[]
        for num in nums:
            c=abs(num)-1
            if nums[c]>0:
                nums[c]=-nums[c]
        for i in range(len(nums)):
            if nums[i]>0:
                x.append(i+1)
        return x