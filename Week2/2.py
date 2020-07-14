'''
Link: https://www.codechef.com/LRNDSA02/problems/PSHOT
'''

from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    n=int(stdin.readline())
    s=stdin.readline()

    ha=0;la=n;hb=0;lb=n;
    ans=2*n

    for i in range(2*n):
        if i%2==0:
            if s[i]=='1':
                ha+=1
            la-=1
        else:
            if s[i]=='1':
                hb+=1
            lb-=1
        
        if (ha-hb>lb) or (hb-ha>la):
            ans=i+1
            break
    
    
    stdout.write(str(ans)+'\n')
