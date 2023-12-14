# CTI-110
 # P4HW1 - Score List
 # Wright Jacob
 # 10/20/23
 # Ask user to enter scores
scores = int(input("How many scores would you like to enter?"))
score = 0
total = 0
for score in range(scores):
    print("Enter Score: ")
    score = float(input())
    while score < 0 or score > 100:
     print("Try Again. Please enter a score in range 0 to 100")
  # ask user to input again
     print("Enter score again: ")
     score = int(input())
     print("--------RESULTS---------")
     total = min[scores]
"""print("Enter grade for Module 1:  ")
module1 = float(input())
print("Enter Grade for Module 2:  ")
module2 = float(input())
print("Enter Grade Module 3:  ")
module3 = float(input())
print("Enter Grade for Module 4:  ")
module4 = float(input())
print("Enter Grade for Module 5:  ")
module5 = float(input())
print("Enter Grade for Module 6:  ")
module6 = float(input())
# put data(grades) in a list
grades = [module1, module2, module3, module4, module5, module6]
"""







"""if answer == sum:
  print("NICE! You are correct!")
elif answer != sum:
  print("That answer is incorrect.")
  print("\t ", num_1, sep="")
  print("  -\t", num_2)
  print("Try again ")
  answer = int(input())
  """