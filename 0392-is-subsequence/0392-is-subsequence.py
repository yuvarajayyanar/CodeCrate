class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1=0
        p2=0
        while p1<len(s):
            if p2>=len(t):
                return False
            if s[p1]==t[p2]:
                p1+=1
                p2+=1
            else:
                p2+=1
        return True
