"""
CTI 110
P5T1 - Functions
Wright Jacob
10/24/23
"""

def main():
  print("Hello World!")
  burger = 4.958513
  print_money(burger)  
  print_money(9)
  print_money(33.44)
# main() ends when wee stop indenting
# other functions
def print_money(amount):
  print("$", format(amount, ".2f"), sep="") # to take spaces out use , sep="")... to compress output together on same line use end=""
  
# Now, start the program
main()





