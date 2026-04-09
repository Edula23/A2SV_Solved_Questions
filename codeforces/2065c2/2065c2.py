t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()
    prev = float('-inf')
    
    for v in a:
        
        left, right = 0, m-1
        ans = float('inf')
        
        while left <= right:
            mid = (left + right)//2
            if b[mid] - v >= prev:
                right = mid - 1
            else:
                left = mid + 1
        
        if v >= prev:
            ans = v
            
        if left < m:
            curr = b[left] - v
            if curr >= prev:
                ans = min(ans, curr)
        print(ans, v)
        if ans == float('inf'):
            print("NO")
            break
        prev = ans
    else:
        print("YES")