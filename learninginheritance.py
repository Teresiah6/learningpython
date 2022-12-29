# class that inherits is the subclass and class inherited from is the superclass
class Animal:

    def __init__(self, birthType="unknown", appearance="unknown", blooded="unknown"):
        self.birthType = birthType
        self.appearance = appearance
        self.blooded = blooded

    # getter methods
    @property
    def birthType(self):
        return self.__birthType

    # setters
    @birthType.setter
    def birthType(self, birthType):
        self.__birthType = birthType

    # appearance
    @property
    def appearance(self):
        return self.__appearance

    # setters
    @appearance.setter
    def appearance(self, appearance):
        self.__appearance = appearance

    # blooded
    @property
    def blooded(self):
        return self.__blooded

    # setters
    @blooded.setter
    def blooded(self, blooded):
        self.__blooded = blooded

    # magic method string magic method used to cast our object as a string
    def __str__(self):
        return "A {} is {} it is {} it is {}".format(type(self).__name__, self.birthType, self.appearance, self.blooded)


class Mammal(Animal):
    def __init(self, birthType="born alive", appearance="hair or fur", blooded="warm blooded", nurseYoung=True):
        Animal.__init__(self, birthType, appearance, blooded)
        self.__nurseYoung = nurseYoung

    # set getters and setters for nurse young
    @property
    def nurseYoung(self):
        return self.__nurseYoung

    @nurseYoung.setter
    def nurseYoung(self, nurseYoung):
        self.__nurseYoung = nurseYoung

    '''
    you can also overwrite any methods from the classes you inherit from
    overwriting magic str
    '''

    @property
    def __str__(self):
        return super().__str__() + " and it is {} they nurse their young".format(self.nurseYoung)


class Reptile(Animal):
    def __init__(self, birthType=" born in an egg or born alive", appearance="dry scales", blooded="cold blooded"):
        Animal.__init__(self, birthType, appearance, blooded)

    # No need for function overloading in python uses splat ie *args to tke in an unknown no of args
    def sumAll(self, *args):
        sum = 0

        for i in args:
            sum += i

        return sum

#demo of polymorphism in python
def getBirthType(theObject):
        print("the {} is {}". format(type(theObject).__name__, theObject.birthType))


def main():
    animal1 = Animal("born alive", "hair or fur")


    print(animal1.birthType)
    #calling the magic string
    print(animal1)

    human = Mammal()
    print(human.birthType)
    print(human.appearance)
    print(human.blooded)
   #print(human) problem with nurseYoung
    #print(human.nurseYoung)
    #print(human.nurseYoung) - problem with nurse young,mammal has no attribute _mammal__nurseYoung
    print()

    snake = Reptile()
    print(snake.birthType)
    print(snake)
    #sumall
    print("Sum: {}".format(snake.sumAll(1,2,3,4,5,6,7,8,9,10)))

    getBirthType(human)
    getBirthType(snake)

main()
