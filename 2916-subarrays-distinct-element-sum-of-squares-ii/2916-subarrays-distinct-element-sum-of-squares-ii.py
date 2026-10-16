class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        sum1 = [0] * (4 * n)   # Sum of distinct counts
        sum2 = [0] * (4 * n)   # Sum of squared distinct counts
        lazy = [0] * (4 * n)   # Lazy propagation

        def apply(node, l, r, val):
            length = r - l + 1

            # Use the old sum1 before updating it
            sum2[node] = (
                sum2[node] + 2 * val * sum1[node]
                + val * val * length
            ) % MOD

            sum1[node] = (sum1[node] + val * length) % MOD
            lazy[node] = (lazy[node] + val) % MOD

        def push(node, l, r):
            if lazy[node] == 0 or l == r:
                return

            mid = (l + r) // 2
            val = lazy[node]

            apply(node * 2, l, mid, val)
            apply(node * 2 + 1, mid + 1, r, val)

            lazy[node] = 0

        def update(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                apply(node, l, r, 1)
                return

            push(node, l, r)
            mid = (l + r) // 2

            if ql <= mid:
                update(node * 2, l, mid, ql, qr)

            if qr > mid:
                update(node * 2 + 1, mid + 1, r, ql, qr)

            sum1[node] = (
                sum1[node * 2] + sum1[node * 2 + 1]
            ) % MOD

            sum2[node] = (
                sum2[node * 2] + sum2[node * 2 + 1]
            ) % MOD

        last = {}
        ans = 0

        for r, x in enumerate(nums):
            p = last.get(x, -1)

            # Add one distinct element to starts in [p + 1, r]
            update(1, 0, n - 1, p + 1, r)

            # Sum of squares of all subarrays ending at r
            ans = (ans + sum2[1]) % MOD

            last[x] = r

        return ans