"""CTI-110
P3HW2 - Salary/ P4HW2
Wright JAcob
10/4/23
"""
total_emp = 0
total_ot = 0
total_reg = 0
total_gross = 0
name = str(input("Employee name:"))
while name!= "Done":
# Ask user to enter employee name
  
  #Ask user to enter number of hours the employee worked this week
  hrs = float(input("Hours worked this week:"))
  #Ask user to enter employee's pay rate
  rate = float(input("Employee Pay Rate:"))
  print("-"*40)
  overtime_hrs = hrs - 40
  if overtime_hrs < 0:
     overtime_hrs = 0
  overtime_pay = overtime_hrs * 26.25
  reg_h_pay = 40 * rate
  gross = overtime_pay + reg_h_pay
  print("Employee Name:", name)
  print("hours\t","Pay Rate\t","Overtime\t ","Overtime Pay\t","Reg Pay\t","Gross Pay\t")
  print("-"*80, "\n")
  print(hrs,"\t ", rate,"\t ", overtime_hrs,"\t ", overtime_pay,"\t ", reg_h_pay,"\t ", gross)
  name = str(input("Employee name:"))
  hrs = float(input("Hours worked this week:"))
  #Ask user to enter employee's pay rate
  rate = float(input("Employee Pay Rate:"))
  print("-"*40)
  overtime_hrs = hrs - 40
  if overtime_hrs < 0:
     overtime_hrs = 0
  overtime_pay = overtime_hrs * 26.25
  reg_h_pay = 40 * rate
  gross = overtime_pay + reg_h_pay
  print("Employee Name:", name)
  print("hours\t","Pay Rate\t","Overtime\t ","Overtime Pay\t","Reg Pay\t","Gross Pay\t")
  print("-"*80, "\n")
  print(hrs,"\t ", rate,"\t ", overtime_hrs,"\t ", overtime_pay,"\t ", reg_h_pay,"\t ", gross)
# total hr and OT pay/hrs
  total_emp += 1
  total_ot += overtime_pay
  total_reg += reg_h_pay
  total_gross += gross
  print("Employees Entered: ", total_emp)
  print("Paid for Overtime: ", total_ot)
  print("Paid for regular hours: ", total_reg)
  print("Paid in Gross: ", total_gross)
# end of loop
