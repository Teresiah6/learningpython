class Dog:
    #static variable - going to be shared every object of type dog ever created
    num_of_dogs = 0
    def __init__(self, name="unknown"):
        self.name=name
#keep track of num of dogs
        Dog.num_of_dogs += 1

    @staticmethod
    def getNumofDogs():
        print("there are currently {} dogs".format(Dog.num_of_dogs))

def main():
    spot = Dog("Spot")
    doug = Dog("Doug")

    #get num of dogs
    spot.getNumofDogs()
    doug.getNumofDogs()
main()