# Anonymous function is a Lambda....

"""f = lambda a : a*a

result=f(5)

print(result)"""


# Using "Filter,Map,Reduce function "
# Filtering a Even Number
"""def is_even(n):
    return n%2==0
nums=[2,3,4,5,6,7,8,9,10]
evens=list(filter(is_even,nums))

print(evens)"""

# Using "Lambda..."
# Filtering a Odd Number

"""num=[1,2,3,4,5,6,7,8,9,10]
odds=list(filter(lambda n : n%2!=0,num))
print(odds)"""

# Here we doubles the value where we get from odds.


"""num=[1,2,3,4,5,6,7,8,9,10]

odds=list(filter(lambda n : n%2!=0,num))

doubles=list(map(lambda n : n*2,odds))

print(doubles)"""

# Here we use Reduce function.

from functools import reduce

num=[1,2,3,4,5,6,7,8,9,10]

odds=list(filter(lambda n : n%2!=0,num))

doubles=list(map(lambda n : n*2,odds))
print(doubles)

sum = reduce(lambda a,b : a+b,doubles)

print(sum) 