'''
#finally is used when you always want certain ccode to exception whether or not an exception
#is raised or not
'''
num1, num2 = input("Enter 2 values to divide: ").split()
try:
    quotient = int(num1) / int(num2)
    print(f"{num1} / {num2} = {quotient}")
except ZeroDivisionError:
    print("You cannot divide by zero")
else:
    print("You didn't raise an exception")
finally:
    print("I execute no matter what")