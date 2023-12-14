"""
CTI 110
P5QUIZ - Length, Width, Area
Jacob Wright
Brian Delrosario
Thu 11/9/2023
"""

def getLength():
    length = float(input("Enter length of rectangle: "));
    return length

def getWidth():
    width = float(input("Enter width of rectangle: "));
    return width

def getArea(length, width):
    area = length * width
    return area

def displayData(length, width, area):
    print(f'Length: {length}');
    print(f'Width: {width}');
    print(f'Length: {area}');
    

def main():
  
  length = getLength()
  width = getWidth()
  area = getArea(length, width)

  displayData(length, width, area)

# start the program
main()
