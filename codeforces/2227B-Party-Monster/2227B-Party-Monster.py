import sys
input = sys.stdin.readline

from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right


def solve():
    # write your logic here
    n = int(input())
    bracket = input()
    if bracket.count(')') != bracket.count('('):
        print('NO')
    else:
        print('YES')
    
    

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()