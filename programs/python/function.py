def greet():   #creating a function
    print("Haiii...",end="")
    print("Suriya.R")
#greet()    calling a function


  # check the given number is odd or even

"""def even_odd(i):
    if  num %2==0:
        print("It is Even Number")
    else:
        print("It is Odd Number")   

num=int(input("Enter a number:"))          
even_odd(num)"""


# In python we do not use pass by value and pass by referance
#immutable "int,string,tuple"
#Mutable "List,Set,dict"
def update(x): 
   print (id(x))
   x=8
   print (id(x))
   print(x)

a=10
print (id(a))
update(a) 
print(a)


# Check Odd or Even using function
"""
x=int(input("Enter a Number: "))
def checkOddEven(x):
    if(x % 2 == 0):
      print("Even")
      return 
    else:
      print("Odd")
checkOddEven(x) """