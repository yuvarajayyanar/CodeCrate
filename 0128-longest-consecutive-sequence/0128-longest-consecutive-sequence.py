class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr=set(nums)
        l=0

        for num in arr:
            if num-1 not in arr:
                curr=num
                c=1
                while curr+1 in arr:
                    curr+=1
                    c+=1
                l=max(l,c)

        return l