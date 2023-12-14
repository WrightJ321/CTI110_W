# CTI 110
# P4T2
# Time Card
# WrightJ
# 10/19/23

# This program will act like a time card reader,
# adding up each day's hours to get the total.

# Version 1 - uses numbers for days
# change line below if it's a 7 day week
DAYS_IN_WEEK = 5
totalHours = 0 #  the total starts at zero

print("Please enter your hours worked.")

for day in range(DAYS_IN_WEEK):
    print("Hours for day", day+1, ": ", end="")
    hoursToday = float(input())
  #input vaidation is a loop inside this loop
    while hoursToday < 0 or hoursToday > 24:
     print("You cant work negative hrs or over 24 hrs. Please enter in range of 0-24 hrs")
     # ask again
     print("Hours for day", day+1, ": ", end="")
     hoursToday = float(input())
    totalHours = totalHours + hoursToday # add to running total

# print the total
print("You worked a total of", totalHours, "hours this week.")

# print the average
avgHours = totalHours / DAYS_IN_WEEK
print("For an average of", format(avgHours, "0.2f"), "hours per day.")
# Show how printing money works (Format method)
per_hour =  10.00
gross_pay = per_hour * totalHours
print("If you made $ ", format(per_hour,"0.2f"), " per hr")
print("Your gross pay would be $", format(gross_pay), "0.2f")

  