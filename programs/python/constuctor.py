"""class Computer:
    def __init__(self):
        self.name="Suriya"
        self.age=21
    def update(self):
        self.age=25
    def compare(self,other):
        if c1.age == other.age:
            return True
        else:
            return False

c1=Computer()
c2=Computer()

if c1.compare(c2):
    print("There are same")


print(c1.name)
print(c2.age)"""


# Types of Variable: 
# 1. Instance Variable
# 2. Class (Static) Variable

# namespace is an area where you create and store object/variable.

"""class car:
     
    wheel=4              # Outside the Function: It is Class variable


    def __init__(self):

        self.mil=10            # inside the Function: It is Instance Variable
        self.com="BMW"
    
c1=car()
c2=car()

c2.com="Rolls Roys"

car.wheel=5

print(c1.mil,c1.com,c1.wheel)
print(c2.mil,c2.com,c1.wheel)"""


# Types of Methods:
# 1. Instance Methods
        # -> Accessor Methods
        # -> Mutator Methods
# 2. Class Methods
# 3. Static Methods

"""class Student:

    School='Trinity'

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return(self.m1+self.m2+self.m3/3)
    
    def get_m1(self):
        return self.m1          # geter...(Only feach the value not change the value."Accessor Method")
                                # seter....(Change the value."Mutator Method")

    def set_m1(self,value):
        self.m1=value


    @classmethod
    def getSchool(cls):
        return cls.School
    

    @staticmethod
    def info():
        print("This is Static Class....")



s1=Student(44,55,66)
s2=Student(77,88,99)

print(s1.avg())
print(s2.avg())

print(Student.getSchool())
Student.info()"""


class Student:
    def __init__(self,name,rolno):         # You can create object of inner class inside the outer class.
                                                                 # or 
                                            # You can create object of inner class outside the outer class provided you use outer class name to call it.
        self.name=name
        self.rolno=rolno
        self.lap=self.Laptop()
    

    def show(self):
        print(self.name,self.rolno)
        self.lap.show()
        
    class Laptop:
        def __init__(self):
            self.brand='Lenovo'
            self.cpu='i5'
            self.ram=8

        def show(self):
            print(self.brand,self.cpu,self.ram)


s1=Student("Suriya",52)
s2=Student("Aravind",10)

s1.show()

"""lap=s1.lap
lap=s2.lap"""

#lap=Student.Laptop()

