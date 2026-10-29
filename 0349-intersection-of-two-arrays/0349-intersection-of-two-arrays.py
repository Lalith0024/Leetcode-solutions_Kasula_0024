class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # hash1 = {}
        # hash2 = {}
        # # fill hash 
        # for i in nums1:
        #     if i not in hash1:
        #         hash1[i] = 0
        #     hash1[i] +=1

        # for i in nums2:
        #     if i not in hash2:
        #         hash2[i] = 0
        #     hash2[i] +=1
        # # make arrays of what exist (instead you could also make into set and convert back to array same size, number of loops reduces)
        # arr1 = hash1.keys()
        # arr2 = hash2.keys()
        # ans = []
        # for i in arr1:
        #     if i in arr2:
        #         ans.append(i)
        #     else:
        #         continue 
        # return ans

        # space -> o(n+n+n+n+n)
        # time -> o(n+n+(n**2))
        return list(set(nums1) & set(nums2))