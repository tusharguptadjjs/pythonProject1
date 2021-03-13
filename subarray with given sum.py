def subarray(a,s,n):

    for i in range(n):
        cm=a[i]
        j=i+1
        while j<=n:
           if cm == s:
               print("sum found between")
               print("indexes %d and %d"%(i,j-1))
               return 1
           if cm >sum or j==n :
               break
           cm = cm + a[j]
           j=j+1

    print("no subarray found")
    return 0


a=[1,2,3,7,5]
s=12
n=len(a)
subarray(a,s,n)


