n, m  = input().split()
for i in range(int(n)):
    if i % 2 == 0:
        print('#'*int(m))
    elif (i+1) % 4 == 0:
        print('#'+'.'*(int(m)-1))
    else:
        print('.'*(int(m)-1) + '#')