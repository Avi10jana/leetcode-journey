class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1
        
        odd_count = sum(1 for c in cnt if c % 2 == 1)
        if n % 2 == 0 and odd_count != 0:
            return ""
        if n % 2 == 1 and odd_count != 1:
            return ""
        
        mid_char = None
        if n % 2 == 1:
            for i in range(26):
                if cnt[i] % 2 == 1:
                    mid_char = chr(97 + i)
                    break
        
        half = [c // 2 for c in cnt]
        h = n // 2
        t = target
        
        # max feasible prefix length matching t[0:h] using half-counts
        work = half[:]
        L = 0
        for i in range(h):
            idx = ord(t[i]) - 97
            if work[idx] > 0:
                work[idx] -= 1
                L = i + 1
            else:
                break
        
        def build_from_H(H_list):
            Hs = ''.join(H_list)
            if n % 2 == 1:
                return Hs + mid_char + Hs[::-1]
            else:
                return Hs + Hs[::-1]
        
        # Case B: full prefix match
        if L == h:
            H = list(t[:h])
            P = build_from_H(H)
            if P > t:
                return P
        
        # Case A: deviate at position i (largest feasible i first)
        upper = min(L, h - 1) if h > 0 else -1
        for i in range(upper, -1, -1):
            work = half[:]
            for j in range(i):
                idx = ord(t[j]) - 97
                work[idx] -= 1
            
            target_idx = ord(t[i]) - 97
            chosen = -1
            for c in range(target_idx + 1, 26):
                if work[c] > 0:
                    chosen = c
                    break
            if chosen == -1:
                continue
            
            work[chosen] -= 1
            H = list(t[:i]) + [chr(97 + chosen)]
            rest = []
            for c in range(26):
                rest.extend([chr(97 + c)] * work[c])
            H.extend(rest)
            return build_from_H(H)
        
        return ""