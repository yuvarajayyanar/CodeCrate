class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        y=len(needle)
        for i in range(len(haystack)):
            if haystack[i:i+y]==needle:
                return i
            else:
                continue
        return -1