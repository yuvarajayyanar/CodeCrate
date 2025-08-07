class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1={}
        
        for i in range(len(nums1)):
            if nums1[i] in d1:
                d1[nums1[i]]+=1
            else:
                d1[nums1[i]]=1
        result = []
        for num in nums2:
            if num in d1 and d1[num] > 0:
                result.append(num)
                d1[num] -= 1

        return result