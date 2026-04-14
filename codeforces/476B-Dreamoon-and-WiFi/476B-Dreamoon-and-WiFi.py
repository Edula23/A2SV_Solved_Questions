def recurse(curr, n):
    if n >= len(s2):
        res.append(curr)
        curr = 0
        return
    else:
        if s2[n] == '+':
            recurse(curr+1, n+1)
        elif s2[n] == '-':
            recurse(curr-1, n+1)
        else:
            recurse(curr+1, n+1)
            recurse(curr-1, n+1)
recurse(0, 0)
ans = res.count(val)
print(ans/ len(res))