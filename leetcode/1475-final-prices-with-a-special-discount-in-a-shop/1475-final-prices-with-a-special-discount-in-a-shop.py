class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for i in range(len(prices)):
            while stack and prices[i] <= stack[-1][0]:
                prices[stack[-1][1]] -= prices[i]
                stack.pop()
            stack.append([prices[i], i])
        return prices



 

        