class Zerodenerror(Exception):
    pass

while True:
    try:
        num = int(input("enter the numerator"))
        num2 = int(input("enter the denominator"))
        if num2 == 0:
            raise Zerodenerror("it should not be zero")
        value = num/num2
        print(value)
        break
    except Zerodenerror:
        print("no")