class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        par = self.kthGrammar(n-1, (k+1)//2)
        if k % 2 == 0:
            if par == 0:
                return 1
            else:
                return 0
        else:
            return par