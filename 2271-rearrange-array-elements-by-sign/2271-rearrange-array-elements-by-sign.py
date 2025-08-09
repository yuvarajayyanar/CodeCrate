class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        arr=[0]*(n)

        p1=0
        p2=1

        for num in nums:
            if num>0:
                arr[p1]=num
                p1+=2
            else:
                arr[p2]=num
                p2+=2
        return arr