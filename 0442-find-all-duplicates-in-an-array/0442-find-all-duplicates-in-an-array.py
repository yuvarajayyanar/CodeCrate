class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        d={}

        result=[]
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        for key in d:
            if d[key] > 1:
                result.append(key)
                
        return result
