class Solution:
    def countCommas(self, n: int) -> int:
        

        # numbers in range [1000,100000] have one comma so subract them from 1000 +1 ?
        
        
        if n<1000:
            return 0
        else:
            ans = n+1-1000
            return ans


        