#solve for x
#x +4 = 9
# x will always be the 1st value recieved and
#you will only deal with addition

#receive a string and split it into the variables
#convert the string into ints
#concvert the result into  astring and join it to the string
# "X ="
#print()
#create a function
def solve_eq(equation):
    x, add, num1, equal, num2 = equation.split()
    num1, num2 = int(num1), int(num2)
    return "x = " + str(num2 - num1)

print(solve_eq("x + 4 = 9"))



'''
my solution - wrong 
receiving = input("enter an equation ie (x + 4 = 9")
receiving = receiving.split()
for i in receiving:
    if i.isalnum():
        int(i)
    else:
        print(i)
print("X = " )
'''
