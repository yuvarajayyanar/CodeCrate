class Solution:
    def longestPalindrome(self, s: str) -> str:
        x=s[0]
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                t=s[i:j]
                if t==t[::-1] and len(t)>len(x):
                    x=t
                else:
                    continue

        return x