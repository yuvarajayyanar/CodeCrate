class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d1={}
        d2={}
        for i in range(len(s)):
            ch1,ch2=s[i],t[i]
            if ch1 in d1:
                if d1[ch1]!=ch2:
                    return False
            else:
                d1[ch1]=ch2
            if ch2 in d2:
                if d2[ch2]!=ch1:
                    return False
            else:
                d2[ch2]=ch1

        return True
        
