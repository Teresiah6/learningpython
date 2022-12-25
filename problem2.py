# we'll provide different ouput based on age
# 1- 18 -> important
#21, 50, 65 -> important
#aall others -> Not important
#receive age and store in age
age = eval(input("Enter age: "))
#eval allows for automatic conversion of strings to integers
# check age 1 to 18
if(age >= 1) and (age <=18):
    print("Important Birthday")
#else 21 and 50
elif (age == 21) or (age == 50):
    print("Important Birthday")
#check if age is not less than 65 ie greater than 65
elif not( age < 65):
    print("Important Birthday")
else:
    print("Sorry Not Important Birthday")
