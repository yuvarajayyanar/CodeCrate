class Solution:
    def judgeCircle(self, moves: str) -> bool:
        c=0
        prev=""
        for ch in moves:
            if ch=="R":
                c+=1
            elif ch=="L":
                c-=1
            elif ch=="U":
                c+=100
            else:
                c-=100
        if c==0:
            return True
        else:
            return False