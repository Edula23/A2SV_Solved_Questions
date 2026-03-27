class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backTrack(num, path):
            if len(path) == k:
                ans.append(path[:])
                return
            for i in range(num, n+1):
                path.append(i)
                backTrack(i+1, path)
                path.pop()
        ans = []
        backTrack(1, [])
        return ans