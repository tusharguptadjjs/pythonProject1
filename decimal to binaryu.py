def dectobinary(n):
    if n>=1:
        dectobinary(n//2)
        print(n%2,end=' ')
n=int(input())
dectobinary(n)