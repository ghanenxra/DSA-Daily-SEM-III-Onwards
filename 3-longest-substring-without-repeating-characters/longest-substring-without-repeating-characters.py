class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_elements=set()
        l=0
        maxx=0

        for t in range(len(s)):

            while s[t] in unique_elements:
                unique_elements.remove(s[l])
                l+=1

            unique_elements.add(s[t])

            maxx=max(maxx, t-l+1)
        return maxx