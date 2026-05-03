class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        outgraph = [[] for _ in range(len(graph))]
        outgoing = [0 for _ in range(len(graph))]
        res = []
        for i in range(len(graph)):
            outgoing[i] += len(graph[i])
            for v in graph[i]:
                outgraph[v].append(i)
        queue = deque()
        for i in range(len(outgoing)):
            if outgoing[i] == 0:
                queue.append(i)
        while queue:
            node = queue.popleft()
            res.append(node)
            for n in outgraph[node]:
                outgoing[n] -= 1
                if outgoing[n] == 0:
                    queue.append(n)
        return (sorted(res))
            


        
        