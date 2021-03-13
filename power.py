def power(x,n):
    if n==0:
        return 1
    else:
        return x*power(x,n-1)
ans = power(7.7,2)
print(ans)
