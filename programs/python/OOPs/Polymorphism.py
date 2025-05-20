# Note- Polymorphism means Many Form (Poly = Many, Morph ism = Form)

# We implement this is 4 type

# 1. Duck Typing
# 2. Operator Overloding
# 3. Method Overloading
# 4. Method Overriding

# > Duck Typing

"""class VS():
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor():
    def execute(self):
        print("Spell Check")
        print("Convention check")
        print("Compiling")
        print("Running")

class Laptop():
    def code(self,ide):                        # IDE = Integrated Development Environment
        ide.execute()

ide=MyEditor()

lap1=Laptop()

lap1.code(ide)"""

# > Operator Overloding

"""a=10
b=11

print(a+b)          # Both will give the same output 21,21....

print(int.__add__(a,b))"""  # Behind the screen this function is calling to add the two number.       # we can use __sub__(), __mul__() ect....


"""class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self,other):             # Operator Overloding
        m1=self.m1 + other.m1
        m2=self.m2 + other.m2
        s3=student(m1,m2)

        return s3

s1=student(50,60)
s2=student(70,80)

s3=s1+s2

print(s3.m1)

print(s3.m2)"""

# -> Method Overloading and Method Overriding

"""class student:                        This is a concept of method overloading
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def sum(self,a=None,b=None,c=None):
        
        s=0
        if a!=None and b!=None and c!= None:
            s= a+b+c

        elif a!=None and b!=None:
            s= a+b
        
        else:
            s=a

        return s

s1=student(50,50)

print(s1.sum(10))"""
    
# -> Method Overriding

class A:
    def show(self):
        print("In A Show")

class B(A):
    def show(self):           # This show overrides the above show method. If we don't any show method here it show above method.
        print("In B Show")
    

a1=B()
a1.show()