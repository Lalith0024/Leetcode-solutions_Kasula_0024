class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        memo = [[False] * n for _ in range(n + 1)]
        intv = []

        for l in range(1, n + 1):
            for i in range(l - 1, n):
                if l == 1:
                    memo[l][i] = True
                elif l == 2:
                    memo[l][i] = s[i - 1] == s[i]
                else:
                    memo[l][i] = (
                        s[i - l + 1] == s[i]
                        and memo[l - 2][i - 1]
                    )

                if memo[l][i] and l >= k:
                    intv.append((i - l + 1, i))

        intv.sort(key=lambda x: x[1])

        ans = 0
        last_end = -1

        for start, end in intv:
            if start > last_end:
                ans += 1
                last_end = end

        return ans