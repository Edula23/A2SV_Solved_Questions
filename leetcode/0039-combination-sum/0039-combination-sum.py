class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backTrack(n, tot, path):
            nonlocal ans
            if tot == target:
                ans.append(path[:])
                return
            if n == len(candidates) or tot > target:
                return

            path.append(candidates[n])
            backTrack(n, tot+candidates[n], path)
            path.pop()
            backTrack(n+1, tot, path)
        backTrack(0, 0, [])
        return ans

