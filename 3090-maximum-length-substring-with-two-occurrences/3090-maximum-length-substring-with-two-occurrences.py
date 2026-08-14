class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        char_freq={}
        left=0
        res=0
        for right in range(len(s)):
            char_freq[s[right]]=char_freq.get(s[right],0)+1
            
            while char_freq[s[right]]>2:
                char_freq[s[left]]-=1
                left+=1
            if char_freq[s[right]]<=2:
                res=max(res,right-left+1)
        return res