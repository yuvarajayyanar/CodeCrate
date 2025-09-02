class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_sum=float('inf')

        for i in range(len(nums)-2):
            l,r=i+1,len(nums)-1

            while l<r:
                m=nums[l]+nums[i]+nums[r]
                if abs(m-target)<abs(min_sum-target):
                    min_sum=m
                if m<target:
                    l+=1
                elif m>target:
                    r-=1
                else:
                    return min_sum

        return min_sum

