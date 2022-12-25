#enter a string in uppercase:
secret_mes = input("Enter a string to hide in uppercase: ")
hidden_message = ""
for char in secret_mes:
    hidden_message += str(ord(char)-23)
print("secret_mes: ", hidden_message, end="")
print()
#print(secret_mes)

#cycle back and create the message two at a time
secret_mes = ""
for i in range (0, len(hidden_message)-1, 2):
    char_code = hidden_message[i] + hidden_message[i+1]
    secret_mes += chr(int(char_code)+ 23)
print("Original Message: ", secret_mes )
