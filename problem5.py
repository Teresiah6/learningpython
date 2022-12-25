#Have the user  enter their investment amount and expected interest rate
#Each year their investment will increase by their investment + their investment * interest rate is
# print out the earnings after a 10 year period
investment= input("Please enter your investment: ")
interest = input("please enter the interest rate: ")
investment = float(investment)
interest = float(interest) * .01

for i in range(10):
    investment = investment + (investment * interest)

print(f" You earned: {investment:.2f} ")


#mistakes made: Introduced a new val earnings. and put print in the loop
