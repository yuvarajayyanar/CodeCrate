class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if len(s)<k:
            return 0
        d={'a','e','i','o','u'}
        c=0
        for i in range(k):
            if s[i] in d:
                c+=1
        r=c

        for i in range(k,len(s)):
            if s[i] in d:
                c+=1
            if s[i-k] in d:
                c-=1
            if c>r:
                r=c
        return r
                


