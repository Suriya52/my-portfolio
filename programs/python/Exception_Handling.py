# Errors are Three types :
# 1. Compile Time Error
# 2. Logical Error
# 3. Run Time Erroe

a=5
b=2

try:
    print("Resource open")
    print(a/b)
    k=int(input("Enter a Number:"))
    print(k)

except ZeroDivisionError as e:        # It is executed only when the error occurs.
    print("Hey you cancont divide a Number by zero",e)

except ValueError as e:
    print("Invalid Input...")

except Exception as e:
    print("Something Went Wrong....")

finally:                 # Finally block will be executed if we get error as well as if we don't get the error
    print("Resource Closed")
