class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        class unionFind:
            def __init__(self, n):
                self.root = [i for i in range(n)]
                self.size = [1] * n
            def find(self, x):
                if x == self.root[x]:
                    return x
                return self.find(self.root[x])
            def union(self, x, y):
                rootx = self.find(x)
                rooty = self.find(y)

                if rootx != rooty:
                    if self.size[rootx] > self.size[rooty]:
                        self.root[rooty] = rootx
                        self.size[rootx] += self.size[rooty]
                    else:
                        self.root[rootx] = rooty
                        self.size[rooty] += self.size[rootx]
        n = len(isConnected)
        dsu = unionFind(n)
        res = n

        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] and dsu.find(i) != dsu.find(j):
                    res -= 1
                    dsu.union(i, j)
        return res

            
            

