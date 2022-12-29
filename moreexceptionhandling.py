'''exceptions are going to be triggered either when an error occurs
or when you want a exception to be triggered
exceptions are used to handle errors, execute specific code, execute code when smth happens'''
try:
    #problematic code here
    aList = [1,2,3]
    print(aList[3])
#multiple exceptions
#except (IndexError, NameError)
except IndexError:
    print("Sorry that index doesn't exist")
except:
    print("An unknown error occurred")
