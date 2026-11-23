class Solution:
    def func(self, stype, s):
        maxlen = 0
        pal = str()
    
        for i in range(len(s)):
            if stype == "even":
                l, r = i, i + 1
            else: 
                l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxlen:
                    maxlen = r - l + 1
                    pal = s[l : r + 1]

                l -= 1
                r += 1
        return pal

    def longestPalindrome(self, s: str) -> str:
        even_pal = self.func("even", s)
        odd_pal = self.func("odd", s)

        if len(even_pal) > len(odd_pal):
            return even_pal
            
        return odd_pal
