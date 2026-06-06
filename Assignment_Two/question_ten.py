# 10. Student Performance Ranking System
# Write a Python program that processes marks of multiple students.
# Requirements:
# ● Create a function that accepts a list of marks.
# ● Use loops to calculate grades:
# ○ A → 80 and above
# ○ B → 60–79
# ○ C → 40–59
# ○ F → Below 40
# ● Use a lambda function to sort marks in descending order.
# ● Display:
# ○ Sorted marks
# ○ Grade distribution
# ○ Number of passed students

def analyze_marks(marks):
    sorted_marks = sorted(marks, key=lambda x: x, reverse=True)

    grade_distribution = {"A": 0, "B": 0, "C": 0, "F": 0}
    passed_students = 0

    for mark in marks:
        if mark >= 80:
            grade_distribution["A"] += 1
            passed_students += 1
        elif mark >= 60:
            grade_distribution["B"] += 1
            passed_students += 1
        elif mark >= 40:
            grade_distribution["C"] += 1
            passed_students += 1
        else:
            grade_distribution["F"] += 1

    print("\nSorted Marks (Descending):", sorted_marks)
    print("\nGrade Distribution:")
    for grade, count in grade_distribution.items():
        print(f"{grade}: {count}")

    print("\nNumber of Passed Students:", passed_students)

n = int(input("Enter number of students: "))

marks = []
for i in range(n):
    mark = int(input(f"Enter marks of student {i+1}: "))
    marks.append(mark)

analyze_marks(marks)