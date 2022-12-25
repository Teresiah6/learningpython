#create a customer list
#create an array of customer dictionaries
customers = []
while True:
    createEntry = input("Enter Customer? (Yes/No): ")
    createEntry = createEntry[0].lower()


    #leave loop if no
    if createEntry == 'n':
        break
    elif createEntry == '' or createEntry.strip() =='' or createEntry[0] == '':
        print("please pick a yes or no")
    else:
        fName, lName = input("Enter customer name: ").split()
        customers.append({"fName ": fName, "lName " : lName})

#print customers
for cust in customers:
    print(cust['fName'], cust['lName'])
'''customer = []
iscustomer = input("Customer: Yes/No")
customerName = {}
while iscustomer == "yes":
    customerName = input("Enter Customer Name: ")
    customerName = str(customerName)
customer.append(customerName)
print(customer)
'''