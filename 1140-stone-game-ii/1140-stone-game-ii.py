class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp: list[list[list[int]]] = [[[-1] * (len(piles)+1) for _ in range(0, 2)] for _ in range(0, len(piles)+1)]
        person: int = 1
        M: int = 1
        i: int = 0
        # alice = 1, bob = 0
        alice_max_score: int = self.helper(i, person, M, piles, dp)
        return alice_max_score

    def helper(self, i: int, person: int, M: int, piles: list[int], dp) -> int:
        if i >= len(piles):
            return 0

        if dp[i][person][M] != -1:
            return dp[i][person][M]

        stone: int = 0
        res: int = -1 if person == 1 else float("inf")

        x: int = 1
        while x <= min(2*M, len(piles)-i):
            stone += piles[i +x -1]

            if person == 1:
                # alice turn
                res = max(res, stone + self.helper(i+x, 0, max(x, M), piles, dp))
            else:
                # bob turn
                res = min(res, self.helper(i+x, 1, max(x, M), piles, dp))

            x += 1

        dp[i][person][M] =  res

        return res