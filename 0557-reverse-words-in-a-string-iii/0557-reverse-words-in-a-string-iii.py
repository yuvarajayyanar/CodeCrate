class Solution:
    def reverseWords(self, s: str) -> str:
        p1=0
        l=list(s)
        n=len(l)
        for p2 in range(n+1):
            if p2==n or l[p2]==" ":
                left,right=p1,p2-1

                while left<right:
                    l[left],l[right]=l[right],l[left]
                    left+=1
                    right-=1
                p1=p2+1
        return "".join(l)