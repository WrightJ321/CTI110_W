"""
CTI-110
P3Lab2 - Letter Grades
wrightj
9/28/23
Convert a number grade into a letter grade. (ten point scale)
"""


print("Enter the number grade: ")
num_grade = int(input())

letter_grade = "G"
# do conversion
if num_grade >= 90:
  letter_grade = "A"
elif num_grade >= 80:
  letter_grade = "B"
elif num_grade >= 70:
  letter_grade = "C"
elif num_grade >= 60:
  letter_grade = "D"
elif num_grade <= 59:
  letter_grade = "F"
  # or else statement (else: letter_grade = "F")
  

# Print the letter grade
print("A grade of", num_grade, "is a", letter_grade)



