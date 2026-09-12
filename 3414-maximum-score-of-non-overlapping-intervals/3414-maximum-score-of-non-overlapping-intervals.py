class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        intervals = [a+[i] for i,a in enumerate(intervals)]
        intervals.sort(key = lambda x:(x[1]))
        lefts = [l for l,r,a,i in intervals]
        rights = [r for l,r,a,i in intervals]
        weights = [a for l,r,a,i in intervals]
        indices = [i for l,r,a,i in intervals]
        n = len(intervals)
        @cache
        def dp(i,remain):
            if i < 0 or remain == 0:
                return 0,tuple([])
            resval,reslist = dp(i-1,remain)
            j = bisect.bisect_right(rights,lefts[i]-1)
            resval2,reslist2 = dp(j-1,remain-1)
            resval2 += weights[i]
            reslist2 = tuple(sorted([indices[i]]+list(reslist2)))
            if resval2>resval or (resval2 == resval and reslist2<reslist):
                resval,reslist = resval2,reslist2
            return resval,reslist
        return list(dp(n-1,4)[1])



        