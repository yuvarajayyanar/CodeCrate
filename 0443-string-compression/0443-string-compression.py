class Solution:
    def compress(self, chars: List[str]) -> int:
        p1=0
        p2=0

        while p1<len(chars):
            ch=chars[p1]
            c=0
            while p1<len(chars) and chars[p1]==ch:
                c+=1
                p1+=1
            
            chars[p2]=ch
            p2+=1
            if c>1:
                for digit in str(c):
                    chars[p2]=digit
                    
                    p2+=1
            
        del chars[p2:]
        return p2

