class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        adjList = defaultdict(list)
        res = 0
        for i in range(len(bombs)):
            for j in range(i+1, len(bombs)):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                d = sqrt((x1-x2)**2 + (y1-y2)**2)
                if r1 >= d:
                    adjList[i].append(j)
                if r2 >= d:
                    adjList[j].append(i)
        def dfs(i, visited):
            if i in visited:
                return 0
            visited.add(i)
            for bom in adjList[i]:
                dfs(bom, visited)
            return len(visited)
        for i in range(len(bombs)):
            res = max(res, dfs(i, set()))
        return res