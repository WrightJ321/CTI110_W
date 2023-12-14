# CTI-110
# P4T3 - Three loops 
# WrightJ
# 10/10/23

# Write three loops
# 1. for loop
# 2. while loop
# 3. while with sentinel
# For each of these, do the following
# Ask the user how many cars they saw today
# Find the total and the average
day = 1
MAX_DAYS = 5
cars_today = 0
cars_total = 0
# 1 - For loop
print("Enter how many cars you saw each day")
for day in range(1, MAX_DAYS+1):
  print("Day #", day, end=": ")
  cars_today = int(input())
  cars_total = cars_total + cars_today
# Print the total
print("Total number of cars seen: ", cars_total)
avg = cars_total / MAX_DAYS
print("Average per day", avg)

# 2 - While loop
day = 1
cars_today = 0
cars_total = 0
print("Enter how many cars you saw each day")
while day <= MAX_DAYS:
  print("Day #", day, end=": ") # the end= cleans up the output, refer to the output ran
  cars_today = int(input())
  cars_total = cars_total + cars_today
  day = day + 1
print("Total number of cars seen: ", cars_total)
avg = cars_total / MAX_DAYS
print("Average per day", avg)

# Take 3 - "Sentinel"
cars_total = 0 
print("\n\nEnter -1 to finish")
DONE_VALUE = -1 # if they type this, finish
# go until they say to stop with DONE_VALUE
keep_going = True 
days = 0
while keep_going:
  print("Cars seen today: ", end="")
  cars_today = int(input())
  if cars_today == DONE_VALUE:
    # exit
    keep_going = False
  else:
    # add the value to the total
    cars_total = cars_total + cars_today
    days = days + 1
print("total cars = ", cars_total)
print("over", days, "days")
avg = cars_total / days
print("Average: ", avg)
