# Decorators.....

"""def div(a,b):
    print(a/b)

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return  inner

div=smart_div(div)

div(2,4) """

# There is a Saying that goes like "when I worte this Code only God and I understood what it did...
#                                                       And Now only God Knows...."

# Modules we use our own Modules here "calc" is our own modules.

from calc import *
a=10
b=20
c=mul(a,b)
print(c)