class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        res = defaultdict(set)

        for src, dst in edges:
            graph[dst].append(src)

        def dfs(i, curr):
            if not graph[i]:            
                return

            for par in graph[i]:
                if par not in res:
                    dfs(par, set())

                curr = curr | res[par]
                curr.add(par)
            res[i] = curr

        for i in range(len(graph)):
            ans = set()
            dfs(i, ans)
        return ([sorted(res[i]) for i in range(n)])