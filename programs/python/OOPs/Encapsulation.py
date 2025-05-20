# Encapsulation is Binding of Variables and Methods

class Car:
    def __init__(self,carname,no_of_wheels,no_of_airbags):
        print("This is a constructor!")
        self.__no_of_wheels = no_of_wheels
        self.no_of_airbags = no_of_airbags
        self.mileage = 20.0
        self.carname = carname

    def __del__(self):
        print("This is a Destructor!",self)

    def __str__(self):
        return(self.carname)

    def movingforword(self,speed):
        print("Car is moving with a speed of",speed)

    def movingbackword(self):
        print("Car is moving backward")

    #getter
    def get_no_of_wheels(self):
        print ("No of wheels:",self.__no_of_wheels)

    #setter
    def set_no_of_wheels(self):
        self.__no_of_wheels=no_of_wheels


Car1= Car("RollsRoy",4,6)
print(Car1)
print(Car1.mileage,Car1.get_no_of_wheels(),Car1.no_of_airbags)

Car2=Car("BMW",5,10)
print(Car2.mileage,Car2.get_no_of_wheels(),Car2.no_of_airbags)

#Car1.set_no_of_wheels(7)    This is for set or update the value.
#print(Car1.get_no_of_wheels())