"""
CTI-110
P3HW2 - Salary
Wright JAcob
10/4/23
"""


# Ask user to enter employee name
name = str(input("Employee name:"))
  #Ask user to enter number of hours the employee worked this week
hrs = float(input("Hours worked this week:"))
  #Ask user to enter employee's pay rate
rate = float(input("Employee Pay Rate:"))
print("-"*40)
overtime_hrs = hrs - 40
if hrs > 40:
  #Calculate employee's gross pay
  gross_pay = (40 * rate) + (overtime_hrs * (rate * 1.5))
else:
  #Calculate employee's gross pay
  gross_pay = hrs * rate
  #Calculate employee's net pay
  net_pay = gross_pay - (gross_pay * .25)
  #Print employee's name, hours worked, pay rate, gross pay, and net pay
  print("Employee Name:", name)
else:

total_pay = hrs * rate
print("Employee Name:", name)
print("Hours Worked:", hrs)
print("Pay Rate:", rate)
print("Gross Pay:", total_pay)
if overtime_hrs < 0:
 overtime_hrs = 0
 overtime_pay = overtime_hrs * rate * 1.5
 reg_h_pay = hrs * rate
 gross = overtime_pay + reg_h_pay
 print("Employee Name:", name)
 print("hours\t","Pay Rate\t","Overtime\t ","Overtime Pay\t","Reg Pay\t","Gross Pay\t")
 print("-"*80, "\n")
 print(hrs,"\t ", rate,"\t    ", overtime_hrs,"\t     ", overtime_pay,"\t    ", reg_h_pay,"\t    ", gross)  
# Use sentinel loop to end program
done = False
while not done:
  name = str(input("Employee name (or 'done' to exit): "))
if name == 'done':
    done = True
else:
    hrs = float(input("Hours worked this week: "))
    rate = float(input("Employee pay rate: "))
    overtime_hrs = hrs - 40 if hrs > 40 else 0
    overtime_pay = overtime_hrs * rate * 1.5
    reg_pay = hrs * rate
    gross_pay = overtime_pay + reg_pay

    print("Employee Name:", name)
    print("Hours:", hrs)
    print("Pay Rate:", rate)
    print("Overtime Hours:", overtime_hrs)
    print("Overtime Pay:", overtime_pay)
    print("Regular Pay:", reg_pay)
    print("Gross Pay:", gross_pay)
    print("-"*40)
total_emps = str(input())
total_overtime = float(input(f"Total Overtime Hours: {overtime_hrs}"))
total_reg_pay = float(input(f"Total Regular Pay: {reg_pay}"))
total_gross_pay = float(input(f"Total Gross Pay: {gross_pay}"))
if done is True:
    print(f"Total Employees: {total_emps}")
    print(f"Total Overtime Hours: {total_overtime}")
    print(f"Total Regular Pay: {total_reg_pay}")
    print(f"Total Gross Pay: {total_gross_pay}")