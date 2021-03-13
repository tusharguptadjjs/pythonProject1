class student:
    pass_percentage = 30

    def __init__(self, name, percentage, rollno, section):
        self.name = name
        self.percentage = percentage
        self.rollno = rollno
        self.section = section

    def ispass(self):
        if self.percentage >= self.pass_percentage:
            print("passed")
        else:
            print("fail")
    def __add__(self, other):
        print( self.percentage + other.percentage)
        return self.rollno + other.rollno
    def __repr__(self):
        




s1 = student("tushar",77,22,2)
s2 = student("harry",88,33,2)
print(s1 + s2)

