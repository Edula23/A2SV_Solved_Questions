import sys
input = sys.stdin.readline

from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right


def solve():
    v, e = map(int, input().split())
    par = list(range(v))
    edges = []
    size = [1] * v
    res = 0
    
    for _ in range(e):
        s, f, w = map(int, input().split())
        edges.append((w, s-1, f-1))
    edges.sort()
    # print(size, par)
    def find(x):
        if x == par[x]:
            return x
        par[x] = find(par[x])
        return par[x]
    def union(x, y, rx, ry):

        if size[rx] > size[ry]:
            par[ry] = rx
            size[rx] += size[ry]
        else:
            par[rx] = ry
            size[ry] += size[rx]               
        
    
    for e in edges:
        x, y = e[1], e[2]
        rx, ry = find(x), find(y)
        if rx != ry:            
            union(x, y, rx, ry)
            res += e[0]
    print(res)      
    

def main():
    solve()

if __name__ == "__main__":
    main()