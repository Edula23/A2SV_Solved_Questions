class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
                return [1]
        if rowIndex == 1:
            return [1, 1]
        curr = [1, 1]
        init = [1, 1]
        n = 1
        def rec(n, i, j):
            nonlocal init
            if n == rowIndex:
                return curr
            curr[j] = init[i] + init[j]

            if j == len(curr)-1:                
                n += 1
                i, j = -1, 0
                curr.append(1)
                init = curr[:]

            rec(n, i+1, j+1)
        rec(n, 0, 1)
        return init
             
                
            
            