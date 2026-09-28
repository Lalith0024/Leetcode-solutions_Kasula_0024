class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        brackets = []

        for c in s:
            if c == '(':
                brackets.append(c)
                max_depth = max(max_depth, len(brackets))
            elif c == ')':
                brackets.pop()

        return max_depth