"""
CTI-110
P3T2 - Choices and Menus
WrightJ
9/26/23
"""
  # The most simple program, with main()
  
def main():
  # function call, just use the name with the ()
  my_function()
  # Print the menu
  print("-"*10, "Treasure Chest", "-"*10)
  print("1. Sword of the Damned")
  print("2. Enchanted Staff")
  print("3. Shield of the Giant Turtle")
  print("4. Axe of Chaotic Energy")

  
  # Let user choose
  print("Your choice? ", end="")
  choice = int(input())
  print("You chose:", choice)
  
  # branch (if) on weapon
  if choice ==1:
    option_1()
  elif choice ==2:
    option_2()
  elif choice ==3:
    option_3()
  else :
    print("Sorry, You're not worthy of that weapon.")

  
def option_1():
  weapon = ["Sword of the Damned", "Enchanted Staff", "Shield of the Giant Turtle" ]
  print("The weapon you chose is:", weapon[0] )
  print("Would you like to equip your weapon?")
  answer = input()
  if answer == "yes":
    print("Make haste traveler!")
  elif answer == "no":
    print("I grow tired of your antics Traveler.")
  else :
    print("Leave before a curse is placed upon you!")
# 2nd weapon option
def option_2():
  weapon = ["Sword of the Damned", "Enchanted Staff", "Shield of the Giant Turtle" ]
  print("Weapon chosen is:", weapon[1])
  print("Would you like to equip your weapon?")
  answer = input()
  if answer == "yes":
    print("Be sure to read the User's manual!")
  elif answer == "no":
    print("I grow tired of your antics Traveler.")
  else :
    print("Leave before a curse is placed upon you!")
def option_3():
  weapon = ["Sword of the Damned", "Enchanted Staff", "Shield of the Giant Turtle" ]
  print("Weapon chosen is:", weapon[2])
  print("Would you like to equip your weapon?")
  answer = input()
  if answer == "yes":
    print("Beware the Giant Turtle this belonged to, wants it back!")
  elif answer == "no":
    print("I grow tired of your antics Traveler.")
  else :
    print("Leave before a curse is placed upon you!")
def my_function():
  print("This is my function")





# start the program
main()

