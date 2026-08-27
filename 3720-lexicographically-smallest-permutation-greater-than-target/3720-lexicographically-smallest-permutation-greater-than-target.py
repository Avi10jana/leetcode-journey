from functools import lru_cache

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        # Frequency of characters in s
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        @lru_cache(None)
        def dfs(i, greater, state):
            # If all positions are filled, accept only if the string is
            # strictly greater than target.
            if i == len(target):
                return "" if greater else None

            cnt = list(state)

            if greater:
                # Already greater: place the smallest available character.
                for c in range(26):
                    if cnt[c]:
                        cnt[c] -= 1
                        res = dfs(i + 1, True, tuple(cnt))
                        cnt[c] += 1
                        if res is not None:
                            return chr(c + ord('a')) + res
                return None

            # Still equal to target prefix
            t = ord(target[i]) - ord('a')

            for c in range(t, 26):
                if cnt[c] == 0:
                    continue

                cnt[c] -= 1
                res = dfs(i + 1, greater or (c > t), tuple(cnt))
                cnt[c] += 1

                if res is not None:
                    return chr(c + ord('a')) + res

            return None

        ans = dfs(0, False, tuple(freq))
        return "" if ans is None else ans