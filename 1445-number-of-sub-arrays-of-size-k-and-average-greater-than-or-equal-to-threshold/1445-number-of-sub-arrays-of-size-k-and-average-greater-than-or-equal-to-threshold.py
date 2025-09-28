class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sa=sum(arr[:k])
        c=0
        if (sa/k)>=threshold:
            c=1
        for i in range(k,len(arr)):
            sa=sa-arr[i-k]+arr[i]
            if (sa/k)>=threshold:
                c+=1
        return c
        