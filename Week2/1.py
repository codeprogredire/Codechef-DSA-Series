from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    n=int(stdin.readline())
    info=[]
    for _ in range(n):
        val=tuple(map(int,stdin.readline().split()))
        info.append(val)

    profit=float('-inf')

    for v in info:
        temp=(v[1]//(v[0]+1))*v[2]
        profit=max(profit,temp)

    stdout.write(str(profit)+'\n')

