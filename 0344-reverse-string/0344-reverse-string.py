class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n=len(s)-1
        i=0

        while n>i:
            s[n],s[i]=s[i],s[n]
            n-=1
            i+=1