class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        p=n^n>>1
        return (p&(p+1))==0
        