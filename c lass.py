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

    @classmethod
    def change_pass_perc(cls, new_pass_percentage):
        cls.pass_percentage = new_pass_percentage

    @staticmethod
    def behaviour():
            print("behaviour is good")

class programmer(student):
    def __init__(self,name, percentage, rollno, section,languages):
        self.name = name
        self.percentage = percentage
        self.rollno = rollno
        self.section = section
        self.languages = languages
    def printprogdetails(self):
        return f"name is{self.name},percentage is{self.percentage},rollno is {self.rollno},section is {self.section},languages known{self.languages}"










s1 = student("tushar", 66, 77, 3)
s1.change_pass_perc(33)
s1.ispass()
s1.behaviour()
print(s1.name, s1.percentage, s1.rollno, s1.section)
s2=programmer("tushar", 66, 77, 3,["pyhton","c++","c"])
print(s2.printprogdetails())
