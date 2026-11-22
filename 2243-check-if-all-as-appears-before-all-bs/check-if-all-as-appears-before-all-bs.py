class Solution:
    def checkString(self, s: str) -> bool:
        for i in range(len(s)-1):
            if s[i]=="b" and s[i+1]=="a":
                return False
        return True

        # n=len(s)
        # if len(set(s))==1:
        #     return True
        # if len(set(s))!=1:
        #     if s[-1]=="a":
        #         return False
        #     if s[0]=="b":
        #         return False
        
        # for ch in s:


        

