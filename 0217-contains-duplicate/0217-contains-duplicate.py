class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # set equal (time -> same, space extra)
        # sort and check -> (time-> increases, space same)
        # min required 0(n) to traverse and check , try to complete in 0(n) time with 0(1) space 
        # impossible, so just make set, and compare with original:

        set_ = set(nums)
        if len(set_) == len(nums):
            return False
        return True