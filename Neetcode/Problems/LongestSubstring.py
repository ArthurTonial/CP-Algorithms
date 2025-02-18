# https://neetcode.io/problems/longest-substring-without-duplicates

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if len(s) == 0:
#             return 0
        
#         max_length = 1
#         l, r = 0, 1

#         while r < len(s):
#             if s[r] not in s[l:r]:
#                 max_length = max(max_length, r - l + 1)
#             else:
#                 while s[l] != s[r]:
#                     l += 1
#                 l += 1 

#             r += 1
        
#         return max_length

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l, ans = 0, 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            ans = max(ans, len(charSet)) # or r - l + 1
        
        return ans