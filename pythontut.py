#1.asking user for input their name and assign it to var name
#name = input('What is your name? ')
#print('Hello', name)

#2.Ask for input 2 values and store them as num1 and num2
num1, num2 = input('Enter 2 numbers: ').split()
#convert strings to int
num1 = int(num1)
num2 = int(num2)
#find sum
sum = num1 + num2
print(f"{num1} + {num2} = {sum}")