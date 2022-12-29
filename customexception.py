#creating a custom exception DogNameError that inherits from exception
class DogNameError(Exception):
    def __init__(self):
        Exception.__init__(self, *args, **kwargs)
try:
    dogName = input("What is your dogs name: ")
    if any(char.isdigit() for char in dogName):
        #raise an exception custom or inbuilt
       raise DogNameError

except DogNameError:
    print("Your dogs name cannot contain a number")
