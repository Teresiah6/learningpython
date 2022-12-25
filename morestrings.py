rand_string = "       this is an important string     "

#remove the whitespace on left
rand_string = rand_string.lstrip()
#remove the whitespace on left
rand_string = rand_string.rstrip()
#get rid of all the white space
rand_string = rand_string.strip()
#capitalize the first letter
print(rand_string.capitalize())
#make string uppercase
print(rand_string.upper())
#make string lowercase
print(rand_string.lower())
#convert list into a string
a_list = ["Bunch", "of", "random", "words"]
print(" ".join(a_list))
#convert a string into a list
a_list_2 = rand_string.split()
for i in a_list_2:
    print(i)

#count how many times a string occurs in a string
print("How many times is appears: ", rand_string.count("is"))
#get index of random string
print("Where is string: ", rand_string.find("string"))
#replace substring wit substring
print(rand_string.replace("an ", "a kind of  "))
