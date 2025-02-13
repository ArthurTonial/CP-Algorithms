# https://neetcode.io/problems/validate-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = { ')':'(', ']':'[', '}':'{' }
        stack = []

        for c in s:
            if c not in close_to_open:
                stack.append(c)

            else:
                if not stack or stack.pop() != close_to_open[c]:
                    return False
                
        return not stack