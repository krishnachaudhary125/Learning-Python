import re

txt = "My name is Krishna Chaudhary."

x = re.search("\s", txt)

print("first space is located at", x.start())