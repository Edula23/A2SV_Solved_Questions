class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indeg = [0 for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[pre].append(course)
            indeg[course] += 1
        queue = deque()
        for course in range(numCourses):
            if indeg[course] == 0:
                queue.append(course)
        while queue:
            node = queue.popleft()

            for nei in graph[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    queue.append(nei)
        for i in indeg:
            if i > 0:
                return False
        return True
        