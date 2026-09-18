from collections import defaultdict as dd

class Solution:

    def maxNumOfSubstrings(self, s: str) -> list[str]:

        n = len(s)

        first = dd(int)
        last = dd(int)

        # Store first and last occurrence of every character
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i

            last[ch] = i

        candidates = []

        # Generate all valid candidate substrings
        for i in range(n):

            # Only consider the first occurrence
            # of a character as a starting point
            if i != first[s[i]]:
                continue

            end = last[s[i]]
            j = i
            valid = True

            while j <= end and valid:

                # This character appeared before our
                # current starting position, so the
                # substring cannot be valid.
                if first[s[j]] < i:
                    valid = False

                else:
                    # Expand the boundary to include
                    # all occurrences of this character.
                    end = max(end, last[s[j]])

                j += 1

            if valid:
                candidates.append((end, i))

        # Sort by ending index
        candidates.sort()

        res = []
        prev_end = -1

        # Greedily select non-overlapping intervals
        for end, start in candidates:

            if start > prev_end:
                res.append(s[start:end + 1])
                prev_end = end

        return res