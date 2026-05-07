import sys
input = sys.stdin.readline
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right


def solve():
    n = int(input())
    words = [input().strip() for _ in range(n)]
    
    adj = [[] for i in range(26)]
    depend = [0] * 26
    
    for i in range(1, len(words)):
        curr = words[i]
        prev = words[i-1]
        for j in range(len(curr)):
            if j == len(prev):
                break
            if curr[j] != prev[j]:
                asc = ord(curr[j]) % 97
                adj[ord(prev[j]) % 97].append(asc)
                depend[asc] += 1
                break
        else:
            if len(curr) < len(prev):
                print("Impossible")
                return
    res = ""
    # print(adj, depend)
    queue = deque()
    for i in range(26):
        if depend[i] == 0:
            queue.append(i)
    while queue:
        node = queue.popleft()
        res += chr(node + 97)
        for c in adj[node]:
            depend[c] -= 1
            if depend[c] == 0:
                queue.append(c)
    if len(res) != 26:
        print("Impossible")
        return
    print(res)
        

    

def main():
    solve()

if __name__ == "__main__":
    main()