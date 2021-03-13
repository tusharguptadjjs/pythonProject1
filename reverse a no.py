def reversenumber(n):
    rev_no = 0
    while (n>0):
        rem= n%10
        rev_no = (0*10)+rem
        n=n//10
        print(rev_no,end='')
n=int(input("enter  no"))
out = reversenumber(n)
print(out)