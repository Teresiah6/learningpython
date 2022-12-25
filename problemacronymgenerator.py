#Random Access Memory : RAM
#hints
#ask for a string
#convert the string to uppercase
#convert the string to a lists
#cycle through the list
#Get the first letter of the word and eliminate the newline
# addd a newline
string_acronym = input("Enter a string: ")
string_acronym = string_acronym.upper()
string_acronym = string_acronym.split()
for i in string_acronym:
    print(i[0], end="")

print()