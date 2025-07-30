class Solution:
    def isHappy(self, n: int) -> bool:
        d={}

        while n!=1:
            if n in d:
                return False
            d[n]=1

            n=sum(int(digit)**2 for digit in str(n))

        return True

        