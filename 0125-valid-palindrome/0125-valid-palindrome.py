class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        l=0
        r=len(s)-1
        while l<r:

            if not s[r].isalnum() :
                r-=1
            elif not s[l].isalnum():
                l+=1
            elif s[r].lower()==s[l].lower():
                r-=1
                l+=1
            else:
                return False
        return True
