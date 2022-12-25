sample_string = "This is a very important string"
print(sample_string[0])
#last char
print(sample_string[-1])
print(sample_string[9-1])

#sstringlength
print(f"Length = {len(sample_string)}")
#slice
print(sample_string[0:4])
#concatenate
print("Green " + "eggs " + "are " + "real")
#repeat strings several times
print("Hello  " * 5)
#convert an int into a string
num_string = str(4)

#loop throough chars
for char in sample_string:
    print(char)

#cycle through chars in pairs
for i in range(0, len(sample_string)-1, 2):
    print(sample_string[i] + sample_string[i+1])