class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        x={}
        for i,num in enumerate(nums):
            if num in x and i-x[num]<=k:
                return True
            x[num]=i
        return False

                    