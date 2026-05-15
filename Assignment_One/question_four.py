# Mini Login Authentication System
# Build a simple authentication program:
# Store a predefined username and password.
# Take user input.
# Use logical and comparison operators to validate credentials.
# Add another condition:
#   If username correct but password wrong → “Incorrect Password”
#   If username wrong → “User Not Found”

user = "krishna"
psw = "Krishna@123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == "krishna" and password != "Krishna@123":
    print("Incorrect password")

elif username != "krishna":
    print("User not found")

else:
    print("Welcome,",user)