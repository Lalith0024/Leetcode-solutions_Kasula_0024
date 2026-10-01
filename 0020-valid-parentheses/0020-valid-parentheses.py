class Solution:
    def isValid(self, s: str) -> bool:
        li = []
        for ch in s:
            if ch=='(' or ch == '[' or ch == '{':
                li.append(ch)
            else:
                if not li:
                    return False
                c = li[-1]
                if c=='(' and ch == ')':
                    li.pop()
                elif c=='[' and ch == ']':
                    li.pop()
                elif c=='{' and ch == '}':
                    li.pop()
                else:
                    return False
        if not li:
            return True
        return False
        