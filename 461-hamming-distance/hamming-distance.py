class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count=0
        xor=x^y

        while xor>0:
            xor&=xor-1
            count+=1
            
        
        return count