t = int(input())
for _ in range(t):
    n = int(input())
    r = list(map(int , input().split()))
    m = int(input())
    b = list(map(int , input().split()))
    maxr = curr = 0
    maxb = curb = 0
    for i in r:
        curr += i
        maxr = max(maxr, curr)
    for i in b:
        curb += i
        maxb = max(maxb, curb)
    print(maxr + maxb)