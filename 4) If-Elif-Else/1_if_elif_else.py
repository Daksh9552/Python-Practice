#  IF ELSE CONDITIONS

age = int (input ("Enter your age :"))
if age>= 18:
    print ("you are eligible for voting")
else :
    print ("You are not eligible")

#  Discount Checker
amount = float (input ("Enter the total price amount :"))
if amount >=1500:
    print ("You have recieved 15% discount")
else :
    ("You have not recieved any discount")

#  if–elif–else (Multiple Conditions)
marks = float (input ("Enter your marks :"))
if marks>=90 :
    print ("A+")
elif marks >=80 :
    print ("A")
elif marks >=70 :
    print ("B+")   
elif marks >=60 :
    print ("B")
elif marks >=50 :
    print ("C+")
elif marks >=40 :
    print ("C")
else :
    print ("F")

# Sales Performance (Data Analyst Use Case)
sales = 65000
if sales >= 100000:
    print ("High performance")
elif sales >= 50000:
    print ('Moderate performance')
else :
    print ("Poor performance")

#  String Comparison Example
city ="Delhi"
if city=="Delhi":
    print ("City matched")
elif city.lower()== "delhi":
    print("City matched in lower")
else :
    print("city does not matched")

# Password Program
password=input("Enter your password :")

if password=="admin@1":
    print("Login successful")
else:
    print("Wrong Password")

# Email Validation
email = "user@example.com"
if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")


#  Advanced: Missing Data Check
value = "sdf"
if value == "":
    print("Missing Data Found")
else:
    print("Data Available")