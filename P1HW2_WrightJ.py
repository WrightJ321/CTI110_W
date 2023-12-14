# budget calculator
#9/14/2023
# CTI-110 P2HW1- also P1HW2
# Wright, Jacob
# 1. change int to float to change user input to decimal form
# 2. format user input to show dollar sign next to amount of float input


print("What will your budget be for this trip?") 
# budget is 3000
budget = float(input())
print("Where will you be traveling to?")
# destination is California
Destination = input()
print("Will you be traveling by plane or car?")
# traveling by plane but user may spend money on rental car
transportation = input()
if (transportation == "plane"):
  print("Great!")
else:
  print("Road trips create the best memories!")
print("About how much are you willing to pay for gas?")
# cost of gas is 200 via possible rental car
gas = float(input())
print("Almost done! How much are you willing to spend on a hotel?")
# hotel cost is 750
hotel = float(input())
print("Finally! How much are you going to need for food and drinks?")
# food cost is 320
food = float(input())
print("------Travel Expenses------")
print("Trip location:", Destination)
print(f'{"Chosen budget:":<10}${budget}')
print(f'{"Fuel cost:":<10}${gas}')
print(f'{"Hotel:":<10}${hotel}')
print(f'{"Food:":<10}${food}')
print("----------------------------")
remainingbalance = budget - gas - food - hotel
print(f'{"Your remaining balance:":<10}${remainingbalance}')



