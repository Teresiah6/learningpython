#realworld objects have attributes and capabilities
#in oop yyou define the attributes and capabilities
#Dog Attributes (fields or variables in py): Height, Weight, Favorite food
#Dog capabilities (methods /functions): Run, Ealk, Eat
class Dog:
    #self allowa obj to refer to itself to allow for custom dogs e.g dog
    def __init__(self, name= "", height =0, weight= 0):
        #these are attributes of the dog
        self.name = name
        self.height = height
        self.weight= weight

    #define the capabilities
    def run(self):
        print("{} the dog runs".format(self.name))
    #eating
    def eat(self):
        print(f"{self.name} the dog eats")
    #barking
    def bark(self):
        print(f"{self.name} the dog barks")

def main():
    spot = Dog("Spot", 66, 26)
    #call for spot to bark
    spot.bark()
    #another dog
    Simba = Dog("Simba", 90, 50)
    Simba.bark()

main()
