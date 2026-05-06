class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        # print(len(graph))
        def dfs(i, curr):
            nonlocal ans
            if i == len(graph) -1 or len(curr) == len(graph) -1:
                curr.append(i)
                ans.append(curr[:])
                return
            
            curr.append(i)
            # print(curr)
            for val in graph[i]:
                dfs(val, curr)
                curr.pop()

        dfs(0, [])
        return ans
       