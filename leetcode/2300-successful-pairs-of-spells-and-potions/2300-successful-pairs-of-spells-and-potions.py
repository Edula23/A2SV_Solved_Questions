class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        pairs = [0] * len(spells)
        def noSuccess(n):
            low, high = 0, len(potions)-1
            while low <= high:
                mid = (low + high)//2
                if potions[mid] * n < success:
                    low = mid + 1
                else:
                    high = mid-1
            return len(potions) - low

        for i in range(len(spells)):
            pairs[i] = noSuccess(spells[i])
        return pairs
