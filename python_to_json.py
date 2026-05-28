import json

info = {
	"name": "Krishna",
	"age": 21,
	"city": "Lalitpur"
}

x = json.dumps(info)

print(x)