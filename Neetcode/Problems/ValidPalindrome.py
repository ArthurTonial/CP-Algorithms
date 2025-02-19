# https://neetcode.io/problems/is-palindrome

class Solution:
    def isAlphaNumerical(self, c) -> bool:
        if (ord('0') <= ord(c) <= ord('9') or
            ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z')):
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            while not self.isAlphaNumerical(s[l]) and l < r:
                l += 1
            while not self.isAlphaNumerical(s[r]) and l < r:
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        return True
