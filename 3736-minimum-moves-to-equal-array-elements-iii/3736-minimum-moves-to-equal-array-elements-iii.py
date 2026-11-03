class Solution:
    def minMoves(self, nums: List[int]) -> int:
        
        maxi = max(nums)
        ans = 0
        for i in range(len(nums)):
            ans += abs(nums[i]-maxi)
        return ans