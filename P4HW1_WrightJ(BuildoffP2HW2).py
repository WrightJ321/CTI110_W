# CTI-110
# P2HW2 - List
# Wright, J
# Date

# Greeting
# Ask user for each test grade per module, modules 1-6
print("Hey! What's your name?")
user = (input())
print("Nice to meet you", user, "My name is Python.")
print("I can help you out by finding the average of your grades, here. Let me show you.")
#P4HW1 starts
#
#10/28/23
scores_entered = 0
scores = []

print("How many scores would you like to enter?")
scores_entered = int(input())
for score in range(scores_entered):
      print("Enter Score: ")
      score = float(input())
      while score < 0 or score > 100:
       print("Try Again. Please enter a score in range 0 to 100")
    # ask user to input again
       print("Enter score again: ")
       score = float(input())
      scores.append(score)
total_scores= sum(scores)
print("----------Results----------")
print("Lowest Grade:", min(scores))
print("The amount of scores entered:", scores)
average = total_scores / scores_entered
print("Score Average:", round(average, 2))

#print("Highest Grade:",max(scores_entered))
  #sum = module1 + module2 + module3 + module4 + module5 + module6
#average = len(scores) / total
  # P3HW1 - Letter Grade conversion
  # WrightJ
  # 9/28/23
  # Add in Letter Grade Conversion
if average >= 90:
       print("Your Letter Grade average is a(n): A")
elif average >= 80:
       print("Your Letter Grade average is a: B")
elif average >= 70:
       print("Your Letter Grade average is a: C")
elif average >= 60:
       print("Your Letter Grade average is a: D")
elif average <= 59:
       print("Your Letter Grade average is a: F")
       #print("Sum of Grades:", sum)
       round = round(average, 2)
       #print("Average:", round)
       #print("---------------------------")

