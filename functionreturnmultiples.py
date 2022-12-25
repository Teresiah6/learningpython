# a function that returns multiple values
def multi_divide(num1, num2):
    return (num1 * num2), (num1 / num2)

mult, divide = multi_divide(5,4)
print("5 * 4 = ", mult)
print("5 /4 =", divide)