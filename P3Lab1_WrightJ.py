# CTI-110
# M3Lab1- Leap Year
# WrightJ
# 9/21/23

# Calculate if a year is a leap year
# lEAP YEARS ARE:
# Divisible by 4
# unless its a century, then its divisible by 400

# To do: handle the century case

is_leap_year = False

print("What year to check?")
year = int(input())

# if the year is divisible by 4, its a leap year
# We use %, the modulo operator
if year % 4 == 0:
  is_leap_year = True

  # Century exception:
  # if its divisible by 100
  if year % 100 == 0:
  
  # then it isnt a leap year
    is_leap_year = False
  
  # unless its ALSO divisble by 400
  if year % 400 == 0:
  # and then it is a leap year
    is_leap_year = True

  
  # output the answer
  if is_leap_year:
    print(year,"is a leap year.")
  else:
    print(year,"is not a leap year.")
    