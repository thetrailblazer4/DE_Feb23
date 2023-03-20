def search_index(args, target):
	for i, v in enumerate(args):
		if v == target:
			return f"The index of '{v}' is {i}"
	return -1


greeting = 'Hello'

print('Module.....')