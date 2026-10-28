class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:

        mat = []
        for i in range(m):
            mat.append(["#"]*n)
        # go complete right and complete down 
        for i in range(n):
            mat[0][i] = "."
        
        # down 
        for i in range(m):
            mat[i][n-1] = "."
        return ["".join(row) for row in mat]