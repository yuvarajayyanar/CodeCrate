class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        l,r=0,n-1

        while l<r:
            tar=nums[l]+nums[r]
            if tar==target:
                return [l+1,r+1]
                
            elif tar<target:
                l+=1
            else:
                r-=1

            