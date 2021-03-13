class A:
     classvar1 = "i am a class variable  of class A"
     def __init__(self):
         self.var1 = "i am inside class A's constructor"
         self.classvar1 = "instance var"
class B(A):
    classvar1 = "i am a class variable  of class B"
    def __init__(self):
        self.var1 = "i am inside B's constructor"
        self.classvar1 = "instance var B"
a = A()
b = B()
print(b.classvar1)