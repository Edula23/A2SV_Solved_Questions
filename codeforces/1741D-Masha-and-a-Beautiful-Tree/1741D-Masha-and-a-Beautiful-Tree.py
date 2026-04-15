def solve(l, r):
        if l == r:
            return p[l], p[l], 0
        mid = (l+r) // 2
        minL, maxL, lops = solve(l, mid)
        minR, maxR, rops = solve(mid+1, r)
        
        if lops == -1 or rops == -1:
            return 0, 0, -1
        if maxL < minR:
            return min(minL, minR), max(maxL, maxR), rops + lops
        if maxR < minL:
            return min(minL, minR), max(maxL, maxR), rops + lops+1
        else:
            return 0, 0, -1  
    res = solve(0, n-1)   
    print(res[2])