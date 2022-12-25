letter_z = "z"
num_3 = "3.14"
a_space = " "

#find out type of data inside string
print("Is z a letter or number: ", letter_z.isalnum()) #is a letter and num?
print("Is z a letter or number: ", letter_z.isalpha()) #is a letter?
print("Is 3 a number: ", num_3.isdigit()) # a num or int
print("is z a lowercase: ", letter_z.islower())
print("is z a uppercase: ", letter_z.isupper())
print("is a space a space: ", a_space.isspace())
#func
def isfloat (str_val):
    try:
        float(str_val)
        return True
    except ValueError:
        return False

print("is Pi a float: ", isfloat(num_3))




