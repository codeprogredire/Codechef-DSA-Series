'''
Link: https://www.codechef.com/LRNDSA02/problems/COMPILER
'''

from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    expr=stdin.readline().rstrip('\n')
    length=0
    count=0
    for i,v in enumerate(expr):
        if v is '<':
            count+=1
        elif count==0:
            break
        else:
            count-=1
            if count==0:
                length=i+1
    stdout.write(str(length)+'\n')
