class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        n = len(nums)
        sumS = 0
        for i, v in enumerate(nums):
            if n % (i+1) == 0:
                sumS += v**2
        return sumS