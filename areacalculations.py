import math
def get_area(shape):
    shape = shape.lower()
    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    elif shape == "triangle":
        triangle_area()
    elif shape == "parallelogram":
        parallelogram_area()
    else:
        print("Please enter either a rectangle or a circle")

def rectangle_area():
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))

    area = length * width
    print("The area of the rectangle is: ", area)

def circle_area():
    radius = float(input("Enter the radius: "))
    area = math.pi * (math.pow(radius, 2))
    print(f"The area of the circle is: {area:.2f}")

def triangle_area():
    base = float(input("Enter the base length: "))
    height = float(input("Enter the height: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is {area}")

def parallelogram_area():
    base = float(input("Enter the base length: "))
    height = float(input("Enter the height: "))
    area = base * height
    print(f"The area of the parallellogram: {area}")




def main():
    shape_type = input("Get are for which shape: ")

    get_area(shape_type)

main()