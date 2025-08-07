class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num=set(nums2)
        result=[]
        for i in range(len(nums1)):
            if nums1[i] in num:
                if nums1[i] not in result:
                    result.append(nums1[i])
        return result