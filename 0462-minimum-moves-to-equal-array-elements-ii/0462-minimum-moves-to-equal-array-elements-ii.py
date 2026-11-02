class Solution:
    def minMoves2(self, arr: list[int]) -> int:
        # take example of 1, 2, 3
        # instead of making 1->3, 2->3 (min to max)or(max to min)
        # bring all the things to median value 

        arr.sort() 
        if len(arr)%2==1:
            median = arr[len(arr)//2]
        else:
            var1 = arr[(len(arr)//2)-1]
            var2 = arr[len(arr)//2]
            median = (var1+var2)//2
        ans = 0
        for i in arr:
            ans += abs(median-i)
        return ans
