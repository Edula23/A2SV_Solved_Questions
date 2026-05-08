class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        def heapifyD(heap, n, i):
            small = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and heap[left] < heap[small]:
                small = left
            if right < n and heap[right] < heap[small]:
                small = right
            if small != i:
                heap[i], heap[small] = heap[small], heap[i]
                heapifyD(heap, n, small)
        n = len(stones)
        for i in range(n//2 -1, -1, -1):
            heapifyD(stones, n, i)
        i = 0
        while n > 1:
            y = heappop(stones)
            x = heappop(stones)
            if x != y:
                heappush(stones, y-x)
            n = len(stones)
        if not stones:
            return 0
        return -stones[0]
