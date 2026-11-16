class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            new_string=[]

            for i in range(0,len(s),k):
                chunk=s[i:i+k]
                string_sum=str(sum(int(ch)for ch in chunk))
                new_string.append(string_sum)

            s="".join(new_string)
        return s

