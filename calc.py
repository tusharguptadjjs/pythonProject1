n=int(input())
i=1
while i<=n:
    s=1
    while s<=n-i:
        print(" ",end='')
        s=s+1
    j=1
    p=i
    while j<=i:
        print(p,end='')
        j=j+1
        p=p-1
    v=2
    while v<=i:
        print(v,end='')
        v=v+1
    print()
    i=i+1




