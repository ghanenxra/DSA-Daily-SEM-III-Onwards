class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        extra_a=0
        extra_b=0
        for char in s:
            extra_a+=ord(char)
        for char in t:
            extra_b+=ord(char)
        return chr(extra_b-extra_a)

