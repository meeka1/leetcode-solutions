class Solution:
    def maxPower(self, s: str) -> int:
        l = 0
        length = 0

        for r in range(len(s)):
            if s[l] != s[r]:
                l = r
            length = max(length, r-l+1)
        return length