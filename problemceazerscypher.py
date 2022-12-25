#implement a caezar's cypher
#A-Z 65-90
#a-z 97-122
#ord(your_letter)
#chr(your_code)

#check if char is a letter
#don't change space
#Hints
#Use isupper() to decide which unicode to work with
#add the key (num of chars to shift) and if key is bigger or` smaller than
#unicode increase or decrease by decrease
msg = input("Input a message: ")
key = (int(input("How many character should we shift (1-26)?")))

secret_message = ""
for char in msg:
    if char.isalpha():
        char_code = ord(char)
        char_code += key
#forupper case
        if char.isupper():
            if char_code > ord('Z'):
                char_code -=26
            if char_code <ord('A'):
                char_code += 26
#lowercase letters
        else:
            if char_code > ord('z'):
                char_code -= 26
            if char_code < ord('a'):
                char_code += 26
#convert  code to letter and to message
        secret_message +=chr(char_code)
    else:
        secret_message +=char
print("Encrypted: ", secret_message)

#decrypting
key = -key
msg = " "

for char in secret_message:
    if char.isalpha():
        char_code = ord(char)
        char_code +=key
#forupper case
        if char.isupper():
            if char_code > ord('Z'):
                char_code -=26
            if char_code <ord('A'):
                char_code +=26
#lowercase letters
        else:
            if char_code > ord('z'):
                char_code -= 26
            if char_code < ord('a'):
                char_code += 26
#convert  code to letter and to message
        msg +=chr(char_code)
    else:
        msg += char
print("Dencrypted: ", msg)

'''for char in msg_str:
    if char.isalpha():
        ord(char): 
        if msg_str.isupper():
            ord(msg_str) - 26
        else:
            ord(msg_str) +26
print(chr(msg_str))'''