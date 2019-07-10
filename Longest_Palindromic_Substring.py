"""
https://leetcode.com/problems/longest-palindromic-substring/
Runtime: 168 ms, faster than 90.84% of Python online submissions for Longest Palindromic Substring.
"""

class Solution(object):
    def coumptute(self,s,l,r,final):
        while l > 0 and r < len(s) - 1:   
            l -= 1
            r += 1
            if s[l] != s[r]:
                l += 1
                r -= 1
                break
        if len(final) < len(s[l:r+1]):
            return s[l:r+1]
        else:
            return final

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        final = ""
        i = 0
        n = len(s)
        while i < n:
            print(i)
            if i == 0:
                r = 1
                while r < n:
                    if s[i] != s[r]:
                        break
                    r += 1
                final = s[:r]
                i = r - 1
            elif i != n - 1:
                if s[i-1] == s[i+1]:
                    r = i + 1
                    l = i - 1
                    final = self.coumptute(s,l,r,final)
                if s[i] == s[i+1]:
                    r = i + 1
                    l = i
                    final = self.coumptute(s,l,r,final)
            i = i + 1
        return final
