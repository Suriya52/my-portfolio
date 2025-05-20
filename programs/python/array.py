"""from array import *
arr = array('i',[])
num = int(input("Enter a Number of Value:"))
for i in range(num):
    x= int(input("Enter the next Value:"))
    arr.append(x)
print(arr)    

val= int(input("Enter the value for search:"))

k=0
for e in arr:        # Find the index value manuvaly
    if e==val:
         print(k)
         break
    k+=1


print(arr.index(val))   # It find the index value  using Function"""

"""from numpy import *
arr = arange(0,16,5)         
print(arr)"""

from numpy import *

arr1=array([
             [1,2,3],
             [4,5,8],
             [6,7,2],
             [9,10,5]
            ])

arr2=array([
             [2,1,3],
             [5,4,8],
             [7,6,2],
             [10,9,5]
            ])
m=arr1 * arr2;
print(m)            

