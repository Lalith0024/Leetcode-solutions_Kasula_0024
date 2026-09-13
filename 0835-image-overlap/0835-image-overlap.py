class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n=len(img1)
        ones1=[]
        ones2=[]
        for r in range(n):
            for c in range(n):
                if img1[r][c]==1:
                    ones1.append((r,c))
                if img2[r][c]==1:
                    ones2.append((r,c))
        if len(ones1)>len(ones2):
            img1, img2 = img2, img1
            ones1, ones2 = ones2, ones1

        ans=0
        for dr in range(-(n-1),n):
            for dc in range(-(n-1),n):
                overlap=0
                for r,c in ones1:
                    nr=r+dr
                    nc=c+dc
                    if 0 <= nr < n and 0 <= nc < n:
                        if img2[nr][nc]==1:
                            overlap+=1
                ans=max(overlap,ans)
        return ans

        

                

        