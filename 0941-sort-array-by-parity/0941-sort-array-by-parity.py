class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n=len(nums)-1
        x=0
        while x<n:
            if nums[x]%2!=0:
                nums[x],nums[n]=nums[n],nums[x]
                n-=1
            else:
                x+=1 

        return nums