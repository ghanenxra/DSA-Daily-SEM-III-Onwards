class Solution:
    def reverseBits(self, n: int) -> int:
        bin1=bin(n)[2:].zfill(32)
        bin2=bin1[::-1]
        return int(bin2,2)