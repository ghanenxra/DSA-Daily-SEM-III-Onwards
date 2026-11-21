from typing import List


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        orig_children = [[] for _ in range(n)]
        for i in range(1, n):
            orig_children[parent[i]].append(i)

        new_parent = list(parent)
        last_seen = [-1] * 26 

        def dfs_rewire(u: int) -> None:
            idx = ord(s[u]) - ord("a")
            prev_anc = last_seen[idx]

            if prev_anc != -1:
                new_parent[u] = prev_anc

            last_seen[idx] = u
            for v in orig_children[u]:
                dfs_rewire(v)

            last_seen[idx] = prev_anc

        dfs_rewire(0)

        final_children = [[] for _ in range(n)]
        for i in range(1, n):
            final_children[new_parent[i]].append(i)

        ans = [0] * n

        def dfs_size(u: int) -> int:
            size = 1
            for v in final_children[u]:
                size += dfs_size(v)
            ans[u] = size
            return size

        dfs_size(0)
        return ans