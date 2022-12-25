def add_numbers(num1, num2):
    return num1 + num2

print("5 + 4 = ", add_numbers(5,4))

#local variable
'''
def assign_name():
    name = "Douglas"
assign_name()
print(name)
'''

#global variable
'''
doesn't work
def change_name(name):
    name = "Mark"

name = "Tom" #global var
change_name(name)
print(name)

'''
#working
global_name = "Sally"
def change_name():
    global global_name
    global_name = "Sammy"

change_name()
print(global_name)

#not working
def get_sum(num1, num2):
    sum = num1 + num2
    #return sum

print(get_sum(5,4))

