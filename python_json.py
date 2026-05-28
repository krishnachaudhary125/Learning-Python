import json

info = '{"name":"Krishna", "age":21, "city":"Lalitpur"}'
x = json.loads(info)

print("Name :",x["name"], "Age :",x["age"], "City :",x["city"])