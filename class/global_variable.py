x = 100 # GLOBAL - visible everywhere

def show_scope():
	y = 200 # LOCAL - only inside this function
	print(f"Inside: x = {x}, y = {y}") # can see global x

def modify_global():
	global x # declare intent to modify global
	x = 900
	print(f"Modified x to {x}")

show_scope()
modify_global()
print(f"Outside: x = {x}") # x change globally