marks = [70, 50, 65, 90]
total = 0
for i in range(len(marks)):
    print("Subject ",i+1, "  "+"Marks = ", marks[i])
    total = total + marks[i]

print("Total marks : ", total)
percent = (total/400)*100

print("Marks in percentage = ",percent,"%")

if percent > 90:
    print("Distinction")
elif percent >70 and percent <=90:
    print("First Division")
elif percent >50 and percent <=70:
    print("Second Division")
elif percent >40 and percent <=50:
    print("Third Division")
else:
    print("Fail")