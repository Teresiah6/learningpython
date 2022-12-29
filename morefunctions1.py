def mult_by_2(num):
    return num *2

#one way to use functions
times_two = mult_by_2
print("4 * 2 = ", times_two(4))

#pass function into a function
def do_math(func, num):
    return func(num)
print("8 * 2 = ", do_math(mult_by_2, 8))

def get_func_mult_by_num(num):
    #dynamically create a function thats going to receive num and return the whole function and perform custim mult
    def mult_by(value):
        return num * value
    return mult_by
generated_func = get_func_mult_by_num(5)
print("5 * 10 = ", generated_func(10))

#embed function into a data structure
listOfFuncs = [times_two, generated_func]
print("5 * 9 = ", listOfFuncs[1](9))


