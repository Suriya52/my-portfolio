
# 1. Key word variable length argument we can use * , ** to get the value.

"""
def preson (name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)
preson('Suriya',age=20, place='Krishnagiri', phone=9876543210) """

# 2(a). counting number of odd and even number in the input.

"""def count(list):
    even=0
    odd=0
    for i in list:
        if (i % 2 == 0):
            even +=1
        else:
            odd +=1 
    return even,odd

list=[2,3,4,5,6,7,8,9]   
even,odd=count(list)
print("Even={}, odd = {}".format(even,odd))"""

# 2(b). same program geting input from the user.

"""def odd_even(num):
    even=0
    odd=0
    for i in num:
        if (i % 2==0):
            even+=1
        else:
            odd+=1
    return even,odd 
n=input("Enter a list of Number:")            
num = list(map(int, n.split()))
even,odd = odd_even(num)
print("Even:{} Odd: {}".format(even,odd))"""

# 3(a). Fibonacci Sequence. 0 1 1 2 3 5 8 13...

"""def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):    
               c = a + b
               a = b
               b = c 
               print(c)
fib(10)"""

# 3(b). Get input form the user

"""def fib(n):
    a=0
    b=1
    if n==0:
        print(a)
    else:
        print(a)
        print(b)   
        for i in range(2,n):
            c = a + b
            a = b
            b = c 
            print(c)
n=int(input("Enter a Number upto Print the Fibonacci...:") )

fib(n)   """     

# 4(a). Factorial of a number. 

"""def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
x=4
result= fact(x)
print(result)"""

# 4(b).

def fact(n):
    f=1
    for i in range(1,n+1):
        f *=i
    return f
n=int(input("Enter a Number to Factorial:"))
result=fact(n)
print(result)

