class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = {}
        for r, c in reservedSeats:
            if r in reserved:
                reserved[r] |= (1 << c)
            else:
                reserved[r] = (1 << c)
        ans = max(0, n - len(reserved)) * 2
        g1 = (1<<2) | (1<<3) | (1<<4) | (1<<5)
        g2 = (1<<6) | (1<<7) | (1<<8) | (1<<9)
        g3 = (1<<4) | (1<<5) | (1<<6) | (1<<7)
        for r in reserved:
            seats = reserved[r]
            if seats & g1 == 0:
                ans += 1
                seats += 32
            if seats & g2 == 0:
                ans += 1
                seats += 64
            if seats & g3 == 0:
                ans += 1
        return ans