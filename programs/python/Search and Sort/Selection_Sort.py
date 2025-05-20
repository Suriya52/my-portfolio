
def sort(nums):
    for i in range(len(nums)): # We can also use range of 9 because we have nums 
        minpos = i
        for j in range(i,len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

       # print(nums)   This line show all the working process of the this sort

nums=[5,6,2234,564,34,45,6,43345,1,0]
sort(nums)

print(nums)