class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def summ(n):
            s=str(n)
            x=0
            for i in s:
                x+=int(i)
            return x
        for i in range(len(nums)):
            if i==summ(nums[i]):
                return i
        return -1