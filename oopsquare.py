class Square:
    #initialize
    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    #assigning getters
    @property
    def height(self):
        print("Retrieving the Height")
        #use two _ as it is going to be private to protect the data
        return self.__height

#setter
    @height.setter
    def height(self, value):
        #ensure that the value entered is a number
        if value.isdigit():
            self.__height = value
        else:
            print("Please only enter numbers for height")

    #for width
    #getter
    @property
    def width(self):
        print("Retrieving the width")
        # use two _ as it is going to be private to protect the data
        return self.__width

    # setter
    @width.setter
    def width(self, value):
        # ensure that the value entered is a number
        if value.isdigit():
            self.__width = value
        else:
            print("Please only enter numbers for width")

    #get the area
    def getArea(self):
        return int(self.__width ) * int(self.__height)


def main():
    aSquare = Square()

    height = input("Enter Height: ")
    width = input("Enter Width: ")
    aSquare.height = height
    aSquare.width = width

    print("Height: ", aSquare.height)
    print("Width: ", aSquare.width)

    print("The area is: ", aSquare.getArea())
main()

