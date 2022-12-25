#Numbers guessing name
secret_num = 7
while True:
    number = int(input("Guess a number between 1 and 10: "))

    if number == secret_num:
        print("You guessed it")
        break
