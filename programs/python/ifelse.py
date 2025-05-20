"""
var=10
if var > 10:       #---if--else----
    print("Hello")
elif var < 10:
    print("Hello World")
else:
    print("What to Do.. Now..?")   
     
var=10
while var <= 10 and var >= 0:        #---while loop----
    print("Hello World")    
    var=var-1
print("Loop Exited")
"""
""" l=["Apple","Banana","Orange"]       # for loop in list
for i in list(l):
    print("I am eatting {}".format(i)) 

c=["Rolls-Royce","Benz","BMW"]       # for loop in list
for i in c:
    print("I Like  {}".format(i)) 

for r in range(1,10):
    print(r) """

""" for i in range(5):
    for j in range(i+1):
        print("#",end="")
        print() """
"""nums = [1,2,3,4,5,6,10,15]

for num in nums:
    if num % 5 ==0:
        print(num)
        break
else:
        print("Not found")"""
"""
num=10
for i in range(2,num):
     if num % i == 0:
        print("Not a Prime")
        break
else:
      print("It is a Prime")   """         
        
"""from array import *        

vals = array('i',[1,2,3,4,5])

                             loop the arry and print in one by one....
for i in range(len(vals)):
   print(vals[i])

for i in vals:                remove an array index without using an build in function.....
    if i == vals[2]:
        continue
    print(i)"""

"""a=input()                   Error code 
b=""
c=""
for i in a:
    if i.isdigit():
        b=b+i
    else:
        b=b+""
        c=c+i+""
        c=c.split()
        b=b.split()
        for i in range(len(c)):
            print(c[-1]*int(b),end="")   """ 

a = input()                # Refere from chatgpt when we give "3a2b" as a input it give "aaabb" as output
b = ""
c = ""

# Extract digits and letters
for i in a:
    if i.isdigit():
        b += i
    else:
        c += i
        # If c has letters and b has digits, process them
        if b:
            # Print the repeated letters
            print(c[-1] * int(b), end="")
            b = ""  # Reset the digits accumulator

# Ensure that the last accumulated letter (if any) is processed
if b:
    print(c[-1] * int(b), end="")            

    