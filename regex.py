import re

txt = "First, Programming output is Hello World!!"

x = re.search("^First.*World!!$", txt)

print(x)