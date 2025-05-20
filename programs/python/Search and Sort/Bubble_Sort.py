
def sort(nums):
    # outer loop
    for i in range(len(nums)-1,0,-1):  # -1 is index value till 0 , -1 is we are doing in negative oder
        # inner loop
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp



nums=[4,6,7,775,876,2,68,56,22]
sort(nums)

print(nums)

""" 
    Sorting in Function

a=[2,45,5456,45,3424,66,21,5,1,5,354,432,45,66,45]
a.sort()         
print(a)"""