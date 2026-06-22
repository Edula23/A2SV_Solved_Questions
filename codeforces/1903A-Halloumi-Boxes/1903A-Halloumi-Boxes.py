import sys
input = sys.stdin.readline
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right


def solve():
    n, maxx = map(int, input().split())
    arr = list(map(int, input().split()))
    if maxx > 1:    
        return True
    else:
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                return False
        return True
            
    

def main():
    t = int(input())
    for _ in range(t):
        if solve():
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()