class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        st = 0

        for i in range(len(s)):
            ans = 0
            for j in range(st,len(t)):
                if s[i] == t[j]:
                    ans = 1
                    st = j+1
                    break
            # early breaking
            if ans == 0:
                return False
        return True
                

