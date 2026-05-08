class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        ans = []
        visited = set()
        minHeap = [(nums1[0] + nums2[0], (0, 0))]
        visited.add((0, 0))

        while len(ans) < k and minHeap:
            val, (x, y) = heappop(minHeap)
            ans.append([nums1[x], nums2[y]])

            if x + 1 < m and (x+1, y) not in visited:
                heappush(minHeap, (nums1[x+1] + nums2[y], (x+1, y)))
                visited.add((x+1, y))
            if y + 1 < n and (x, y+1) not in visited:
                heappush(minHeap, (nums1[x] + nums2[y+1], (x, y+1)))
                visited.add((x, y+ 1))
        return ans

