# Input & Typecasting 

# 1) String input (Default)
name = input ("enter your name : ")
print ("Welcome", name)


# 2) Typecasting
# string to integer
age = 21
name = "Daksh"
print (name + str(age)) # str is used to convert int to string

# Float to integer
num = 3287.983
print (int (num)) # int is used to convert float to int
print (type(int (num)))


# 3) Input with typecasting
# taking input as an integer
age = int (input ("Enter your age : "))
print ("Your age is",age)
print (type(age))

# taking input as a float
amount = float (input ("Enter the amount :"))
print (amount)
print (type (amount))

# 4) Design a total sales calculator
product = input ("Enter Product Name : ")
quantity = int (input ("Enter no. of product sold : "))
price = float (input ("Enter price per unit : "))

total_sales = quantity * price

print ("_______________________________")
print ("Product :", product)
print ("Total Sales :", total_sales)