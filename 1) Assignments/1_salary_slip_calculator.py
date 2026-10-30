# # Create a Python Program to Generate an Employee Salary Slip

# Taking an required inputs from the user
emp_name = input ("Enter Employee Name : ")
salary = float (input ("Enter Basic Salary : "))
bonus = float (input ("Enter Bonus Amount : "))
tax = float (input ("Enter tax percentage : "))

# calculating elements of salary slip
gross = salary + bonus
tax_amt = (salary * tax)/100
net_salary = gross - tax_amt

# Printing salary slip
print ("________________________________")
print(" ")
print ("Employee Name :", emp_name)
print ("Gross salary :", gross)
print ("Tax Amount :", tax_amt)
print ("Net Salary :", net_salary)