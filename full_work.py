def circle(radius):
    return 3.14159265356 * (radius * radius)
def square(side):
    return side * side
def triangle(base, height):
    return base * height / 2
while True:
    object = str.lower(input("(Triangle, Square or Circle) Please enter the shape you want to find the area of: "))
    if object == "circle":
        radius = int(input("Please enter the radius of the circle: "))
        print(circle(radius))
    if object == "square":
        side = int(input("Please enter the side length of the square: "))
        print(square(side))
    elif object == "triangle":
        base = int(input("Please enter the base length of the triangle: "))
        height = int(input("Please the the height of the triangle: "))
        print(triangle(base, height))
