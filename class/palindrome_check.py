def is_palindrome(txt):
	check = ""
	for char in txt:
		check = char + check
	if txt == check:
		print("True")

is_palindrome("dad")

