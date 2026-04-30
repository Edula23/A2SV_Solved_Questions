import sys
input = sys.stdin.readline
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right


def solve():
    # write your logic here
    
    x, y = map(int, input().split())
    if x % 2 == 1 and y % 2 == 1:
        print("NO")
    else:
        print("YES")    
    
    

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()