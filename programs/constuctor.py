class Computer:
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
print(c2.age)