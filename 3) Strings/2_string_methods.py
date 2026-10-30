#  STRING METHODS (VERY IMPORTANT)

text="       hello python learners       "

# #Remove Spaces
print ("Original text :", text)
print ("Spaces removed :", text.strip())

#Covert to capital letters
print ("Capital text :", text.upper().strip())

#Covert first letter of each word to capital
print ("Propper case :", text.title().strip())

#Covert to Lower case
text2 = text.upper().strip()
print ("Original text :", text2)
print ("lower case :", text2.lower())

#Replace word 'python with SQL'
print ("replaced text :", text.replace("python","SQL").strip())

#Coutn occurrences of a letter of word
print ("No. of 'o':", text.count("o"))

# Check if text start with something
print ("Starts with hello ? :", text.strip().startswith("hello"))

# Check if only numbers are presents in data
mobile="9876543210"
print ("Is the string numeric?", mobile.isnumeric())


msg="Welcome to Python Course"

#Split string into list of words
words = msg.split()
print ("list of words :", words)

#Join back with hyphen
print ("joined message :", "-".join(words))

# Find position of letter p is the msg
print ("index position of 'p':", msg.find("P"))

#Extract domain
email="student@example.com"
print ("domain of email :", email[email.find("@")+1:])



# Advanced Example: Clean Price (Remove Special Characters)
# Example: "Price: ₹3500/-" → "3500"
price_text = "Price: ₹3500/-"
clean = price_text.replace("Price: ₹", "").replace("/-", "")
print ("clean price :", clean)