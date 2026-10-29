class Solution:
    def majorityElement(self, nums: list[int]) -> int:\
    # no space required goal is to complete in 0(n), or o(n) and o(n) space and time 

        maxi = 0
        ans = None
        # ans = None
        # for i in range(len(nums)):
        #     if nums.count(nums[i])>maxi:
        #         maxi = nums.count(nums[i])
        #         ans = nums[i]
        # return ans
        dic = {}

        for i in nums:
            if i not in dic:
                dic[i] = 0
            dic[i] += 1
        for i,j in dic.items():
            if j>maxi:
                maxi = j
                ans = i
        return ans 



        