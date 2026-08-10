class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
        # def dp(i, j, turn, a, b):
            
        #     if i >= len(piles) or j < 0 or j < i:                
        #         return a > b

        #     if turn == 'a':               
        #         return dp(i+1, j, 'b', a+piles[i], b) or dp(i, j-1, 'b', a+piles[j], b)

        #     else:
        #         return dp(i+1, j, 'a', a, b+piles[i]) or dp(i, j-1, 'a', a, b+piles[j])

        
        # return dp(0, len(piles)-1, 'a', 0, 0)
