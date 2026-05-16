# University Grading & AI Recommendation System
# Create a grading system:
# Input marks for Python, Statistics, and Machine Learning.
# Calculate average.
# Assign grades using if-elif-else.
# Additionally:
#   If average > 85 → Recommend “AI Engineer”
#   If average > 70 → Recommend “Data Analyst”
#   Else → Recommend “Software Developer”


python = float(input("Enter marks of python : "))
stat = float(input("Enter marks of statistics : "))
ml = float(input("Enter marks of machine learning : "))

avg = (python + stat + ml)/3

if avg > 85:
    print("AI Engineer")

elif avg > 70:
    print("Data Analyst")

else:
    print("Software Developer")