#eNTER  Calculation: 5 * 6
# 5 * 6 = 30
# store the input of two numbers and the operator
num1, operator, num2 = input('Enter Calculation: '). split()
# convert strings into integers
num1 = int(num1)
num2 = int(num2)
#if + then we need to provide output based on addition
if operator == "+":
    print(f"{num1} + {num2} = {num1+num2}")
elif operator == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operator == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operator == "/":
    print(f"{num1} / {num2} = {num1 / num2}")
elif operator == "**":
    print(f"{num1} ** {num2} = {num1 ** num2}")
elif operator == "//":
    print(f"{num1} // {num2} = {num1 // num2}")
elif operator == "%":
    print(f"{num1} % {num2} = {num1 % num2}")
else:
    print("Error: Operator not found")

# print result
