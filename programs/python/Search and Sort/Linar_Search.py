
pos=-1        # This is in Global Variable

def search(list,n):
    """i=0
                                 This is using While loop
    while i<len(list):
        if list[i]==n:
            globals()["pos"]=i      # This is in Local Variable to access that we want to this.... globals()["Name"]
            return True
        i=i+1
    return False"""

    for i in range(len(list)):      # This is using for loop
        if list[i]==n:
            globals()["pos"]=i
            return True

    return False

list=[3,4,5,6,7,8,9]
n=6

if search(list,n):
    print("Found at",pos)  # This show the value in Index number to make human counting form use "pos+1"
else:
    print("Not Fount")