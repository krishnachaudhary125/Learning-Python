# Student Scholarship Eligibility System
# Create a program that:
# Takes student CGPA, attendance percentage, and number of backlogs as input.
# Uses conditional statements to determine scholarship eligibility.
# Rules:
# CGPA ≥ 3.7, attendance ≥ 85, backlogs = 0 → “Full Scholarship”
# CGPA ≥ 3.2 and attendance ≥ 75 → “Partial Scholarship”
# Otherwise → “Not Eligible”
# Display all values with proper type casting and formatted output.

cgpa = float(input("Enter CGPA:"))
attendance = float(input("Enter attandance percentage: "))
backlog = int(input("Enter number of backlogs: "))

if cgpa>=3.7 and attendance>=85 and backlog == 0:
    print("Full Scholarship")

elif cgpa>=3.2 and attendance>=75:
    print("Partial Scholarship")

else:
    print("Not Eligible")