pos=-1

def search(list,n):
    l=0
    u=len(list)-1

    while l <= u:
        mid = (l+u) // 2

        if list[mid] == n:
            globals()["pos"]=mid
            return True
        else:
            if list[mid] < n:
                l=mid+1
            else:
                u=mid-1
    return False



list=[4,5,8,45,35,67,78,98]
n=98

if search(list,n):
    print("Found at",pos)
else:
    print("Not Found")