# Reverse a String
# Take any string input. Use a for loop to print it character by character in reverse

string = input("Enter string : ")
reversed_string = ""

for char in string:
    reversed_string = char + reversed_string

print("Reversed string :",reversed_string)