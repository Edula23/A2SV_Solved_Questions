n = int(input())
p = []
for _ in range(n-1):
    node = int(input())
    p.append(node)
c = [0] * (n+1)
for i in range(2, n+1):
    parent = p[i-2]
    c[parent] += 1
for i in range(2, n + 1):
    parent = p[i - 2]
    c[parent] += 1
for i in range(1, n + 1):
    if c[i] == 0:
        continue  
    leaf = 0
    for j in range(2, n + 1):
        if p[j - 2] == i and c[j] == 0:
            leaf += 1
    if leaf < 3:
        print("No")
        break
else:
    print("Yes")