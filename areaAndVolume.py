# prints the area and volume of given measured input

# area
def area(length, width):
    return length * width

# perimeter
def perimeter(length, width):
    return 2 * (length + width)

# volume
def volume(length, width, height):
    return length * width * height

# surface area
def surfaceArea(length, width, height):
    return (length * width * 2) + (length * height * 2) + (width * height * 2)

### function that asks for the operation and the inputs
def asksUser():
    operation = str(input("Operation you'd like to? (area, perimeter, volume and surface-area): "))
    if (operation == 'area' or operation == 'perimeter'):
        length = int(input('Length: '))
        width = int(input('Width: '))
        if (operation == 'area'):
            ansArea = area(length, width)
            return f"The area is {ansArea}"
        elif (operation == 'perimeter'):
            ansPeri = perimeter(length, width)
            return f"The Perimeter is {ansPeri}"
    else: 
        length = int(input('Length: '))
        width = int(input('Width: '))
        height = int(input('Height: '))
        if (operation == 'volume'):
            ansVol = volume(length, width, height)
            return f"The Volume is {ansVol}"
        else: 
            ansSA = surfaceArea(length, width, height)
            return f"The Surface Area is {ansSA}"

print(asksUser())
        