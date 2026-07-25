class Solution:
    def maxProduct(self, n: int) -> int:
        nstr = str(n)
        fir = int(nstr[0])
        prev = int(nstr[1])
        for i in range(1, len(nstr)):
            val = int(nstr[i])
            if val >= fir:
                prev = fir
                fir = val
            elif val >= prev:
                prev = val
        return fir * prev
