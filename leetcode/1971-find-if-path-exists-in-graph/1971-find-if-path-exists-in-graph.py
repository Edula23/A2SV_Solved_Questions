class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        a, b = 0, 0
        if len(edges) < 1: 
           if source==destination:
            return True
           else:
            return False
        graph = defaultdict(list)
        for i in range(len(edges)):
            k, v = edges[i]
            graph[k].append(v)
            graph[v].append(k)
            if k == source:
                a, b = i, 0
            elif v == source:
                a, b = i, 1
        def dfs(ver, visited):
            if ver == destination:
                return True
            if len(visited) == n:
                return False
            visited.add(ver)
            for neigh in graph[ver]:
                if neigh not in visited:                    
                    found = dfs(neigh, visited)
                    if found:
                        return True
            return False
        res = dfs(edges[a][b], set())
        return res
                    