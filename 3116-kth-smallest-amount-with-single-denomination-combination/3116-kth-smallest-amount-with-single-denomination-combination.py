class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def f2(coins,i,j,k1,l2=1):
            if(j==0):
                #print(l2,i)
                return k1//l2
            if(i==len(coins)):return 0
            ans=0
            for i2 in range(i,len(coins)):
                ans+=f2(coins,i2+1,j-1,k1,(l2*coins[i2])//gcd(l2,coins[i2]))
            return ans
        def find(coins,k1):
            ans=0
            c1=1
            for i in range(len(coins)):
                ans+=(c1*f2(coins,0,i+1,k1))
                c1*=(-1)
                #print(ans,i+1)
            return ans
        l=1
        coins.sort()
        h=coins[-1]*k+1
        while(l<h):
            mid=(l+h)//2
            f1=find(coins,mid)
           # print(f1,mid)
            if(f1<k):
                l=mid+1
                #print(h,f1,"<>><><")
            else:
                h=mid
        return h

        