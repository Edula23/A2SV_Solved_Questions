class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        row = len(matrix)
        col = len(matrix[0])
        frow, a, b,  = 0, 0, col 
        lcol, c, d = col-1,  1, row-2
        lrow, e, f = row-1, col-1, 0
        fcol, g, h = 0, row-2, 0
        while len(res) < (row  * col):
            for i in range(a, b):
                if len(res) < (row  * col):
                    res.append(matrix[frow][i])
            frow+=1
            a+=1
            b-=1
            for i in range(c, d+1):
                if len(res) < (row  * col):
                    res.append(matrix[i][lcol])
            c+=1
            d-=1
            lcol-=1
            for i in range(e, f-1, -1):
                if len(res) < (row  * col):
                    res.append(matrix[lrow][i])
            lrow-=1
            e-=1
            f+=1
            for i in range(g, h, -1):
                if len(res) < (row  * col):
                    res.append(matrix[i][fcol])
            fcol+=1
            g-=1
            h+=1
        return res






            
            

            


