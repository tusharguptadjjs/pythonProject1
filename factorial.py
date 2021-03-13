def fact(n):
    if n==0 :
        return 0

    return n*fact(n-1)
ans = fact(9)
print(ans)