class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-p for p in piles]

        def heapifyDown(heap, n, i):
            smallest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and heap[left] < heap[smallest]:
                smallest = left

            if right < n and heap[right] < heap[smallest]:
                smallest = right

            if smallest != i:
                heap[i], heap[smallest] = heap[smallest], heap[i]
                heapifyDown(heap, n, smallest)

        n = len(piles)

        # BUILD HEAP MANUALLY
        for i in range(n // 2 - 1, -1, -1):
            heapifyDown(piles, n, i)

        for _ in range(k):
            piles[0] = piles[0] // 2
            heapifyDown(piles, n, 0)

        return -sum(piles)