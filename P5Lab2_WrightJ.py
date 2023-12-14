# CTI 110
# P5LAB2 - Functions
# WrightJ
# 11/2/23

# First, print a table of squares

def main():
  print("P5T2 - Squares")
  print("number\t\tnumber squared")
  for num in range(1, 11): # doiing range 1-11 gives 1-10 (computer reads 0 as a number)
    num_squared = square(num)
    print_row(num, num_squared)
    


# square() is a value returning function
def square(number):
  # input: a number
  # output: the number squared.
  square = number * number
  return square
# print_row() is a void function
def print_row(num, num_squared):
    print(num, "\t\t", num_squared)
  


main()