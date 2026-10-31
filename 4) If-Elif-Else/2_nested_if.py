# 9-Python-Nested IF and Multiple conditions

# CHECKING ELIGIBILITY FOR VOTING
print ("Check your eligibility")
age = int (input ("Enter your age :"))
if age >=18:
    country = input ("Are you a citizen of India ? : Yes/No ")
    if country.lower () == "yes":
        print ("You are eligible for voting")
    else :
        print ("You are not eligible")
else :
    print ("You are underage")

# Multi-Level Verification System
code = int (input ("Enter the security code :"))
if code == 5566:
    department = input ("Enter your department :")

    if department.lower()=="finance" :
        level = int (input ("Enter your access level :"))

        if level >=5:
            print ( "Access Granted: Welcome to the meeting room.")
        
        else :
            print ("Insufficient access level.")

    else :
        print ("Access denied: Department not allowed.")

else : 
    print ("Invalid security code")


#Online Exam Login

reg_no = int (input ("Enter your registration number :"))
if reg_no == 1221:

    sub = input ("Enter your exam subject :")
    if sub.lower() == "python":

        pas = input ("Enter your password :")
        if pas == "8888":
            print ("Login successful! Start your exam.")
        
        else :
            print ("Incorrect password")

    else :
        print("Subject not available")

else :
    print ("Registration Failed")