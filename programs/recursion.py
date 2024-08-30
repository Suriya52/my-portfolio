# We useing an recursion function here to find the factorial of 5.
# Recursion function is a function that call a function itself.

def fact(n):
    if(n==0):
        return 1
    return n * fact((n-1))

result=fact(5)    
print(result)