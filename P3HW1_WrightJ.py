#CTI-110
# P2HW2 - List
# Wright, J
# Date
# Greeting
# Ask user for each test grade per module, modules 1-6
print("Hey! What's your name?")
user = (input())
print("Nice to meet you", user, "My name is Python.")
print("I can help you out by finding the average of your grades, here. Let me show you.")
print("Enter grade for Module 1: ")
module1 = float(input())
print("Enter Grade for Module 2: ")
module2 = float(input())
print("Enter Grade Module 3: ")
module3 = float(input())
print("Enter Grade for Module 4: ")
module4 = float(input())
print("Enter Grade for Module 5: ")
module5 = float(input())
print("Enter Grade for Module 6: ")
module6 = float(input())
# put data(grades) in a list
grades = [module1, module2, module3, module4, module5, module6]
print("----------Results----------")
print("Lowest Grade:", min(grades))
print("Highest Grade:",max(grades))
sum = module1 + module2 + module3 + module4 + module5 + module6
average = sum / len(grades)
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
print("Sum of Grades:", sum)
round = round(average, 2)
print("Average:", round)
print("---------------------------")
