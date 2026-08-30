class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        minIndex = nums.index(min(nums))
        maxIndex = nums.index(max(nums))

        left = min(minIndex, maxIndex)
        right = max(minIndex, maxIndex)

        return min(
            right + 1,
            n - left,
            left + 1 + n - right
        )