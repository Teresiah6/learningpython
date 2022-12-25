#exception habdling forcing them to input a number
while True:
    try:
        number = int(input("Please enter a number: "))
        break

    except ValueError:
        print("You didn't enter a number")

    except:
        print("An unknown error occurred")

print("thank you for enetering a number")