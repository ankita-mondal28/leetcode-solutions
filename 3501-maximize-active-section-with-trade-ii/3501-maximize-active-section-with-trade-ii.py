from bisect import bisect_right
from typing import List

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        starts, ends, typ = [], [], []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            starts.append(i); ends.append(j - 1)
            typ.append(1 if s[i] == '1' else 0)
            i = j
        m = len(starts)
        length = [ends[k] - starts[k] + 1 for k in range(m)]
        total_ones = sum(length[k] for k in range(m) if typ[k] == 1)

        NEG, POS = float('-inf'), float('inf')
        arr0len = [length[k] if typ[k] == 0 else NEG for k in range(m)]
        arr1len = [length[k] if typ[k] == 1 else POS for k in range(m)]
        A = [NEG] * m
        for k in range(1, m - 1):
            if typ[k] == 1:
                A[k] = length[k - 1] + length[k + 1]

        LOG = [0] * (m + 1)
        for k in range(2, m + 1):
            LOG[k] = LOG[k // 2] + 1

        def build_sparse(arr, is_max):
            st = [arr[:]]
            k = 1
            while (1 << k) <= m:
                prev = st[-1]
                half = 1 << (k - 1)
                cur = [None] * (m - (1 << k) + 1)
                for idx in range(len(cur)):
                    a, b = prev[idx], prev[idx + half]
                    cur[idx] = a if (is_max and a >= b) or (not is_max and a <= b) else b
                st.append(cur)
                k += 1
            return st

        st_max_A = build_sparse(A, True)
        st_max_0 = build_sparse(arr0len, True)
        st_min_1 = build_sparse(arr1len, False)

        def query_sparse(st, l, r, is_max):
            if l > r:
                return NEG if is_max else POS
            k = LOG[r - l + 1]
            a, b = st[k][l], st[k][r - (1 << k) + 1]
            if is_max:
                return a if a >= b else b
            return a if a <= b else b

        def find_run(p):
            return bisect_right(starts, p) - 1

        res = []
        for l, r in queries:
            idx_l, idx_r = find_run(l), find_run(r)
            if idx_l == idx_r:
                gain = 0
            else:
                leftLen = ends[idx_l] - l + 1
                rightLen = r - starts[idx_r] + 1
                max0 = NEG
                if typ[idx_l] == 0: max0 = max(max0, leftLen)
                if typ[idx_r] == 0: max0 = max(max0, rightLen)
                if idx_l + 1 <= idx_r - 1:
                    max0 = max(max0, query_sparse(st_max_0, idx_l + 1, idx_r - 1, True))
                min1 = POS
                if idx_l + 1 <= idx_r - 1:
                    min1 = query_sparse(st_min_1, idx_l + 1, idx_r - 1, False)
                gm = NEG
                if idx_l + 1 <= idx_r - 1 and typ[idx_l + 1] == 1:
                    i = idx_l + 1
                    rlen = rightLen if i + 1 == idx_r else length[i + 1]
                    gm = max(gm, leftLen + rlen)
                if idx_l + 1 <= idx_r - 1 and typ[idx_r - 1] == 1:
                    i = idx_r - 1
                    llen = leftLen if i - 1 == idx_l else length[i - 1]
                    gm = max(gm, llen + rightLen)
                if idx_l + 2 <= idx_r - 2:
                    gm = max(gm, query_sparse(st_max_A, idx_l + 2, idx_r - 2, True))
                if min1 == POS:
                    gain = 0
                else:
                    gain_cross = (max0 - min1) if max0 != NEG else NEG
                    gain = max(0, gm, gain_cross)
            res.append(total_ones + gain)
        return res