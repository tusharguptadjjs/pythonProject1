def print1ton(n):
    if n == 0:
        return
    print(n)
    print1ton(n - 1)


print1ton(7)
