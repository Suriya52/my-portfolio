"""class A:       # Super Class                       # Same as B
    def feature1(self):
        print("Feature 1 is Working")
    
    def feature2(self):
        print("Feature 2 is Working")

class B:         # Sub Class                       # In B we can access only this two function/ methods
    def feature3(self):
        print("Feature 3 is Working")
    
    def feature4(self):
        print("Feature 4 is Working")

class C(A,B):                            # It Inheritance the Function "A,B" in C. In C we can access all function.
    def feature5(self):
        print("Feature 5 is Working")
    

a1=A()

a1.feature1() 

b1=B()

b1.feature1()

c1=C()

c1.feature2()
c1.feature4()
c1.feature5()"""



# Here we about "Constructor in Inheritance" and "MRO (Methhod Resolution Order)"

# Note: Sub class can access all the features of Super class BUT Super class can not access any features of Sub class.

class A():
    def __init__(self):
        print("init A")

    def feature1(self):
        print("Feature 1 is Working")

    def feature2(self):
        print("Feature 2 is Working")

class B(A):
    def __init__(self):
        super().__init__()
        print("init B")

    def feature3(self):
        print("Feature 3 is Working")

    def feature4(self):
        print("Feature 4 is Working")
    
a1=B()
    
    