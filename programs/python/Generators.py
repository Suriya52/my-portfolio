"""def TopTen():

    yield 1      # It is a Special KeyWord Which return the value of a number in generator.
    yield 2 
    yield 3  
    yield 4  

values = TopTen()

print(values.__next__())
print(values.__next__())

for i in values:
    print(i)"""


def TopTen():

    n = 1
    while n<=10:
        sq = n*n
        yield sq
        n += 1

values = TopTen()

for i in values:
    print(i)