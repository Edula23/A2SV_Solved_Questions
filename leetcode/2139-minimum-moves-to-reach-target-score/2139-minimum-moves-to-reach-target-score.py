class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        op = 0
        while target > 1:
            if target % 2 == 0 and maxDoubles > 0:
                target = target//2
                op += 1
                maxDoubles-=1
            elif maxDoubles <= 0:
                op += target - 1
                break
            else:
                target -= 1
                op+=1
        return op