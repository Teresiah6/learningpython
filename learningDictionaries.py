#create a dictionary
derekDict = {"fName": "Derek", "lName" : "Banas",
             "address": "123 main St"}
#get values out of a dictionary
print("my name: ", derekDict["fName"])
#change informationnin a dictionary
derekDict["address"] = "215 North st"
#add a key value pair
derekDict['city'] = 'Pittsburgh'
print(derekDict)
#check if infor is present in dict
print("Is there a city: ", "city" in derekDict)
#get list of values in the ctionary
print(derekDict.values())
#list of keys
print(derekDict.keys())
#printing both keys and values
for k, v in derekDict.items():
    print(k, v)
#get value associated with a key and set default
print(derekDict.get("mName", "Not Here"))
print(derekDict.get("lName", "Not Here"))
#delete item in dict
del derekDict["fName"]
for i in derekDict:
    print(i)
#return the first name
derekDict["fName"] = "Derek"
for i in derekDict:
    print(i)
#delete all the data in a dictionary
derekDict.clear()

#create lists that can hold dictionaries
employees = []
#INPUT EMPLOYEE DAta in the list
fName, lName = input("Enter employee name:  ").split()
#add the data entered into employee list
employees.append({"fname": fName, 'lName': lName})
print(employees)