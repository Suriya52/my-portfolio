# Iterators it is like Adding One Number. 

# With Function

"""num=[2,5,7,8,9]

it=iter(num)    # iter is Function.

print(it.__next__()) # It is also a Function 2 Is output

print(it.__next__()) # 5 Is output

print(next(it)) # 7 Is output

for i in num: # 2 5 7 2 5 7 8 9 Is output
    print(i)"""

# Own Iterators

class TopTen:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):

        if self.num <= 10:
            val = self.num
            self.num += 1

            return val
        else:
            raise StopIteration

values = TopTen()

for i in  values:
    print(i)
