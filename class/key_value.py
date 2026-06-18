# Creating a dictionary
student = {
	"name": "Krishna",
	"age" : 21,
	"scores" : [85, 92, 78],
	"active" : True
}

#Access
print(student["name"])
print(student.get("grade", "N/A"))

# Add / Update
student["grade"] = "A"
student["age"] = 22

# nested dict

db = {"u1" : {"name" : "Krishna", "scores" : 90},
	"u2" : {"name" : "Sumit", "scores" : 75}}
print(db["u1"]["scores"])